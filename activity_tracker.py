from log_scraper import scrape
from pathlib import Path

TAG = "TAG"
DATE = "DATE"
TIME = "TIME"
SOURCE = "SOURCE"
MESSAGE = "MESSAGE"

# def zoes_func(log_file, timestamp_start=None, timestamp_end=None):
#     yield [{"2": " "}, {"1": " "}]


# date, time, tag, source, text
def plot(log_file, start=None, end=None):
    time_since_last_commit = 0
    for line in scrape(log_file, start, end):
        print(line)

        time_since_last_commit += 0
        if "COMPILATION STARTED" in line[SOURCE]:
            pass
        if "COMPILATION FINISHED" in line[SOURCE]:
            pass
        if "IDE STARTED" in line[SOURCE]:
            pass
        if "IDE SHUTDOWN" in line[SOURCE]:
            pass
        if "Saving Project" in line[SOURCE]:
            pass
        if "ERROR" in line[TAG]:
            pass
        if "GitHandler" in line[SOURCE]: # we already have commit
            pass


def plot_point(data_generator, start, end):
    time = start
    num_events = 0
    while time < start + 1 and time < end:
        for line in data_generator:
            pass

if __name__ == '__main__':
    home = str(Path.home())

    filename = "/" + home + "/Library/Logs/IdeaIC2019.2/idea.log"
    plot(filename)
