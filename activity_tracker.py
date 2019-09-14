def zoes_func(log_file, timestamp_start=None, timestamp_end=None):
    yield [{"2": " "}, {"1": " "}]


# date, time, tag, source, text
def plot(log_file, start, end):
    time_since_last_commit = 0
    for line in zoes_func(log_file, start, end):
        time_since_last_commit += 0
        if "COMPILATION STARTED" in line["text"]:
            pass
        if "COMPILATION FINISHED" in line["text"]:
            pass
        if "IDE STARTED" in line["text"]:
            pass
        if "IDE SHUTDOWN" in line["text"]:
            pass
        if "Saving Project" in line["text"]:
            pass
        if "ERROR" in line["tag"]:
            pass
        if "commit" in line["text"] and "GitHandler" in line["source"]:
            pass


def plot_point(data_generator, start, end):
    time = start
    num_events = 0
    while time < start + 1 and time < end:
        for line in data_generator:
            pass