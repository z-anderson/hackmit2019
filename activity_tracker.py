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
    df = pd.DataFrame(columns = [TIMESTAMP, TAG, SOURCE, MESSAGE])

    time_since_last_commit = 0
    for line in scrape(log_file, start, end):
        timestamp = datetime.datetime.strptime(line[DATE] + " " + line[TIME], "%Y-%m-%d %H:%M:%S,%f")

        df_row = pd.DataFrame(data = [[timestamp, line[TAG], line[SOURCE], line[MESSAGE]]], columns = [TIMESTAMP, TAG, SOURCE, MESSAGE])
        df = df.append(df_row)

    df.sort_values(by=TIMESTAMP, axis=0, inplace=True)
    return df

def group_by_windows(df):
    print(df)
    columns=["START",  COMPILATION_STARTED, COMPILATION_FINISHED, IDE_STARTED, IDE_SHUTDOWN, SAVING_PROJECT, GIT_HANDLER]
    grouped_df = pd.DataFrame(columns=columns)

    # df.set_index(TIMESTAMP, inplace=True, drop=False)
    start = df.head(1)[TIMESTAMP]
    end = start + datetime.timedelta(hours=1)
    end = pd.Timestamp(end.values[0])

    window = {event : 0 for event in columns}
    window["START"] = start

    print("start", start)
    print("end", end)

    for name, row, in df.iterrows():
        print("timestamp", row.values[0])
        if row.values[0] < end:
            window[row[SOURCE]] += 1
        else:
            print("start new window")
            # concat old window
            window_df = pd.DataFrame(data=window, columns=columns, index = [0])
            grouped_df = grouped_df.append(window_df)

            # set up new window values
            start = row.values[0] # timestamp
            end = start + datetime.timedelta(hours=1)

            window = {event : 0 for event in columns}
            window["START"] = start

            # catch this row
            window[row[SOURCE]] += 1

            print("start", start)
            print("end", end)

    # need to concat at end to not miss last window
    grouped_df = grouped_df.append(window_df)
    return grouped_df

def plot(df):
    print("df", df)
    x = df["START"]
    compilation_started = df[COMPILATION_STARTED]
    copmilation_finished = df[COMPILATION_FINISHED]
    ide_started = df[IDE_STARTED]
    ide_shutdown = df[IDE_SHUTDOWN]
    saving_project = df[SAVING_PROJECT]
    git_handler = df[GIT_HANDLER]

    plt.plot(x, compilation_started, label=COMPILATION_STARTED)
    plt.plot(x, copmilation_finished, label=COMPILATION_FINISHED)
    plt.plot(x, ide_started, label=IDE_STARTED)
    plt.plot(x, ide_shutdown, label=IDE_SHUTDOWN)
    plt.plot(x, saving_project, label=SAVING_PROJECT)
    plt.plot(x, git_handler, label=GIT_HANDLER)

    plt.xlabel('time (hour buckets)')
    plt.ylabel('activity')

    plt.title("Activity Tracker")

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
    window_data = group_by_windows(data)
    plot(window_data)
