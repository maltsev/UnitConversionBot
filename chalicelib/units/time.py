NANOSECOND = (1e-9, ["ns", "nanosecond", "nanoseconds"], "MILLISECOND")
MILLISECOND = (
    0.001,
    ["ms", "millisecond", "milliseconds", "millisec", "msec", "msecs"],
    "SECOND",
)
SECOND = (1, ["s", "second", "seconds", "sec", "secs"], "MILLISECOND")
MINUTE = (60, ["min", "minute", "minutes"], "SECOND")
HOUR = (60 * 60, ["h", "hour", "hours", "hr"], "MINUTE")
DAY = (HOUR[0] * 24, ["d", "day", "days"], "HOUR")
WEEK = (DAY[0] * 7, ["wk", "week", "weeks"], "DAY")
MONTH = (DAY[0] * 30.436875, ["mon", "month", "months"], "DAY")
YEAR = (DAY[0] * 365.2425, ["yr", "year", "years", "y", "yrs"], "DAY")


_BASE = "SECOND"
