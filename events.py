class EventTag:
    def __init__(self, tag_name: str, color_code: str):
        self.tag = tag_name
        self.color = color_code

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


class InfoTag(EventTag):
    def __init__(self, color_code):
        super(InfoTag, self).__init__("INFO", color_code)


class WarnTag(EventTag):
    def __init__(self, color_code):
        super(WarnTag, self).__init__("WARN", color_code)


class ErrorTag(EventTag):
    def __init__(self, color_code):
        super(ErrorTag, self).__init__("ERROR", color_code)


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


class TimeStamp:
    def __init__(self, date: Date, time: Time):
        self.date = date
        self.time = time


class Event:
    def __init__(self, tag: EventTag, time_stamp: TimeStamp):
        self.tag = tag
        self.time = time_stamp