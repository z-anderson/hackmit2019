import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
from log_scraper import scrape

TAG = "TAG"
DATE = "DATE"
TIME = "TIME"
SOURCE = "SOURCE"
MESSAGE = "MESSAGE"

COMPILATION_STARTED = "COMPILATION STARTED"
COMPILATION_FINISHED = "COMPILATION FINISHED"
IDE_STARTED = "IDE STARTED"
IDE_SHUTDOWN = "IDE SHUTDOWN"
SAVING_PROJECT = "Saving Project"
GIT_HANDLER = "GitHandler"

ERROR = "ERROR"
INFO = "INFO"
WARNING = "WARNING"

TIMESTAMP = "TIMESTAMP"

# date, time, tag, source, message
def get_data(log_file, start=None, end=None):
    # counts = {event : 0 for event in {COMPILATION_STARTED, COMPILATION_FINISHED, IDE_STARTED, IDE_SHUTDOWN, SAVING_PROJECT, ERROR, GIT_HANDLER}}

    df = pd.DataFrame(columns = [TIMESTAMP, TAG, SOURCE, MESSAGE])

    time_since_last_commit = 0
    for line in scrape(log_file, start, end):
        timestamp = datetime.datetime.strptime(line[DATE] + " " + line[TIME], "%Y-%m-%d %H:%M:%S,%f")

        df_row = pd.DataFrame(data = [[timestamp, line[TAG], line[SOURCE], line[MESSAGE]]], columns = [TIMESTAMP, TAG, SOURCE, MESSAGE], )
        df = df.append(df_row)

        # print(timestamp)

        # time_since_last_commit += 0
        # if COMPILATION_STARTED in line[SOURCE]:
        #     counts[COMPILATION_STARTED] += 1
        # if COMPILATION_FINISHED in line[SOURCE]:
        #     counts[COMPILATION_FINISHED] += 1
        # if IDE_STARTED in line[SOURCE]:
        #     counts[IDE_STARTED] += 1
        # if IDE_SHUTDOWN in line[SOURCE]:
        #     counts[IDE_SHUTDOWN] += 1
        # if SAVING_PROJECT in line[SOURCE]:
        #     counts[SAVING_PROJECT] += 1
        # if ERROR in line[TAG]:
        #     counts[ERROR] += 1
        # if GIT_HANDLER in line[SOURCE]: # we already have commit
        #     counts[GIT_HANDLER] += 1

    print(df)
    # print(counts)
    # return counts

def plot(data):
    df = pd.DataFrame(data, index=[0])
    print(df)

    x = np.linspace(0, 2, 100)

    plt.plot(x, x, label='linear')
    plt.plot(x, x**2, label='quadratic')
    plt.plot(x, x**3, label='cubic')

    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.title("Simple Plot")

    plt.legend()

    plt.show()



def plot_point(data_generator, start, end):
    time = start
    num_events = 0
    while time < start + 1 and time < end:
        for line in data_generator:
            pass

if __name__ == '__main__':
    filename = "/Library/Logs/IdeaIC2019.2/idea.log"
    data = get_data(filename)
    #plot(data)
