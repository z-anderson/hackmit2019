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

        df_row = pd.DataFrame(data = [[timestamp, line[TAG], line[SOURCE], line[MESSAGE]]], columns = [TIMESTAMP, TAG, SOURCE, MESSAGE], )
        df = df.append(df_row)

    df.sort_values(by=TIMESTAMP, axis=0, inplace=True)
    return df

def group_by_windows(df):
    columns=["START",  COMPILATION_STARTED, COMPILATION_FINISHED, IDE_STARTED, IDE_SHUTDOWN, SAVING_PROJECT, GIT_HANDLER]
    grouped_df = pd.DataFrame(columns=columns)

    # df.set_index(TIMESTAMP, inplace=True, drop=False)
    start = df.head(1)[TIMESTAMP]
    print(start)
    end = start + datetime.timedelta(hours=1)
    print(end)

    window = {event : 0 for event in columns}

    for name, row, in df.iterrows():
        if row.values[0] < pd.Timestamp(end.values[0]):
            window[row[SOURCE]] += 1


    print(window)


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
    group_by_windows(data)
