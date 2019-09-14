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
    def __init__(self, tag: EventTag, time_stamp: TimeStamp, graph_color):
        self.tag = tag
        self.time = time_stamp
        self.graph_color = graph_color

    def get_year(self):
        return self.time.date.year

    def get_month(self):
        return self.time.date.month

    def get_day(self):
        return self.time.date.day

    def get_hour(self):
        return self.time.time.hour

    def get_minute(self):
        return self.time.time.minute

    def get_second(self):
        return self.time.time.second


class IDEStartedEvent(Event):
    def __init__(self, time_stamp: TimeStamp, graph_color):
        super(IDEStartedEvent, self).__init__(InfoTag, time_stamp, graph_color)


class IDEShutdownEvent(Event):
    def __init__(self, time_stamp: TimeStamp, graph_color):
        super(IDEShutdownEvent, self).__init__(InfoTag, time_stamp, graph_color)


class CompilationStartedEvent(Event):
    def __init__(self, time_stamp: TimeStamp, graph_color):
        super(CompilationStartedEvent, self).__init__(InfoTag, time_stamp, graph_color)


class CompilationFinishedEvent(Event):
    def __init__(self, time_stamp: TimeStamp, duration: int, errors: int, warnings: int, graph_color):
        super(CompilationFinishedEvent, self).__init__(InfoTag, time_stamp, graph_color)
        self.duration = duration
        self.errors = errors
        self.warnings = warnings


class SaveEvent(Event):
    def __init__(self, time_stamp: TimeStamp, duration: int, graph_color):
        super(SaveEvent, self).__init__(InfoTag, time_stamp, graph_color)
        self.duration = duration


class ErrorEvent(Event):
    def __init__(self, time_stamp: TimeStamp, text: str, graph_color):
        super(ErrorEvent, self).__init__(ErrorTag, time_stamp, graph_color)
        self.text = text


class GitCommitEvent(Event):
    def __init__(self, time_stamp: TimeStamp, graph_color, time_since_last=None):
        super(GitCommitEvent, self).__init__(InfoTag, time_stamp, graph_color)
        self.duration = time_since_last