#!/usr/bin/env python3
"""
Follow-Through-Day (FTD) detector — bottom-confirmation state machine.

O'Neil's Follow-Through-Day rules (market-bottom confirmation after a correction):
- A potential rally attempt begins on the first up day off a recent low ("Day 1").
- An FTD is a day, typically Day 4 through Day 7 of the attempt, where a major
  index closes UP a significant amount (>= ~1.25% as a common threshold) on
  volume HIGHER than the prior session.
- The rally attempt is reset (invalidated) if the index undercuts the low that
  started the attempt before an FTD prints.
- FTDs that occur very early (Day 1-3) are weaker / less reliable.

This is an OFFLINE calculator: it consumes already-fetched OHLCV history and
returns a state + a 0-100 confirmation score. Feed it data via the data layer.
"""

from __future__ import annotations

FTD_MIN_GAIN_PCT = 1.25          # minimum close-up % to qualify as an FTD
FTD_EARLIEST_DAY = 4             # strongest window starts here
FTD_LATEST_DAY = 7               # classic window ends here (still valid later, weaker)
FTD_MAX_DAY = 13                 # beyond this an attempt is considered stale


def detect_follow_through_day(index_history: list[dict]) -> dict:
    """
    Detect the state of a rally attempt and any Follow-Through-Day.

    Args:
        index_history: list of daily OHLCV dicts ordered MOST RECENT FIRST.
            Each dict needs at least: {"close": float, "low": float, "volume": float}.
            Provide >= 20 sessions for a reliable read.

    Returns:
        dict with state, score (0-100), ftd_day, gain_pct, signal, details.
    """
    if not index_history or len(index_history) < 5:
        return {
            "state": "no_attempt",
            "score": 0,
            "ftd_day": None,
            "gain_pct": None,
            "signal": "Insufficient history to evaluate a follow-through day.",
            "details": [],
        }

    hist = list(reversed(index_history))  # oldest -> newest

    lookback = hist[-20:] if len(hist) >= 20 else hist
    anchor_idx_local = min(range(len(lookback)), key=lambda i: lookback[i]["low"])
    anchor_idx = len(hist) - len(lookback) + anchor_idx_local
    attempt_low = hist[anchor_idx]["low"]

    details = []
    state = "rally_attempt"
    ftd_day = None
    ftd_gain = None
    day_counter = 0

    for i in range(anchor_idx + 1, len(hist)):
        today = hist[i]
        prev = hist[i - 1]
        day_counter += 1

        if today["low"] < attempt_low:
            details.append({
                "day": day_counter,
                "event": "undercut_low",
                "note": "Index undercut the rally-attempt low; attempt reset.",
            })
            return {
                "state": "failed",
                "score": 0,
                "ftd_day": None,
                "gain_pct": None,
                "signal": "Rally attempt failed — prior low undercut before any follow-through day.",
                "details": details,
            }

        gain_pct = (today["close"] - prev["close"]) / prev["close"] * 100.0
        higher_volume = today["volume"] > prev["volume"]
        is_ftd = (
            gain_pct >= FTD_MIN_GAIN_PCT
            and higher_volume
            and day_counter >= FTD_EARLIEST_DAY
        )

        details.append({
            "day": day_counter,
            "gain_pct": round(gain_pct, 2),
            "higher_volume": higher_volume,
            "ftd": is_ftd,
        })

        if is_ftd and ftd_day is None:
            ftd_day = day_counter
            ftd_gain = gain_pct
            state = "confirmed"
            break

        if day_counter >= FTD_MAX_DAY:
            break

    score = _score_ftd(state, ftd_day, ftd_gain)
    signal = _signal_text(state, ftd_day, ftd_gain)

    return {
        "state": state,
        "score": score,
        "ftd_day": ftd_day,
        "gain_pct": round(ftd_gain, 2) if ftd_gain is not None else None,
        "signal": signal,
        "details": details,
    }


def _score_ftd(state: str, ftd_day, gain_pct) -> int:
    if state != "confirmed" or ftd_day is None:
        return 0
    if FTD_EARLIEST_DAY <= ftd_day <= FTD_LATEST_DAY:
        base = 85
    elif ftd_day <= FTD_LATEST_DAY + 3:
        base = 65
    else:
        base = 50
    if gain_pct is not None and gain_pct >= 2.0:
        base = min(100, base + 10)
    return base


def _signal_text(state: str, ftd_day, gain_pct) -> str:
    if state == "confirmed":
        return (
            f"Follow-through day confirmed on Day {ftd_day} "
            f"(+{gain_pct:.2f}% on higher volume) — bottom signal."
        )
    if state == "failed":
        return "Rally attempt failed before any follow-through day."
    return "Rally attempt in progress — no follow-through day yet."


if __name__ == "__main__":
    demo = [
        {"close": 105.0, "low": 104.0, "volume": 1300},
        {"close": 101.0, "low": 100.0, "volume": 1000},
        {"close": 100.5, "low": 99.5, "volume": 900},
        {"close": 100.0, "low": 99.0, "volume": 950},
        {"close": 99.0, "low": 98.0, "volume": 1200},
    ]
    import json
    print(json.dumps(detect_follow_through_day(demo), indent=2))
