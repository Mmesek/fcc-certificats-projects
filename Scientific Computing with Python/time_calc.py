# https://replit.com/@Mmesek/fcc-time-calculator

def add_time(start: str, duration: str, day: str = None) -> str:
    start, day_time = start.split(" ")
    hours, minutes = [int(i) for i in start.split(":")]
    d_hours, d_minutes = [int(i) for i in duration.split(":")]

    total_minutes = hours * 60 + minutes
    total_minutes += d_hours * 60 + d_minutes

    if day_time == "PM" and hours < 12:
        total_minutes += 12 * 60

    days = total_minutes // (24 * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    if hours % 24 >= 12:
        day_time = "PM"
    elif hours % 24 <= 12:
        day_time = "AM"
    hours %= 12

    if hours == 0:
        hours = 12

    result = f"{hours}:{minutes:0>2} {day_time}"

    if day:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        new_day = weekdays[(weekdays.index(day.lower().title()) + days) % len(weekdays)] if days else day
        result += f", {new_day}"

    if days == 1:
        result += " (next day)"
    elif days > 1:
        result += f" ({days} days later)"

    return result


assert add_time("3:00 PM", "3:10") == "6:10 PM", add_time("3:00 PM", "3:10")
assert add_time("11:43 AM", "00:20") == "12:03 PM", add_time("11:43 AM", "00:20")
assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)", add_time("10:10 PM", "3:30")
assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday", add_time("11:30 AM", "2:32", "Monday")
assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)", add_time("11:43 PM", "24:20", "tueSday")
assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)", add_time("6:30 PM", "205:12")
