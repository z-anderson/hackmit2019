from pathlib import Path


def scrape(filename):
    f = open(filename, "r")
    print(f)
    line = f.readline()
    while line:
        for keyword in keywords:
            if keyword in line:
                yield line
        line = f.readline()


if __name__ == '__main__':
    keywords = {"IDE STARTED",
        "COMPILATION FINISHED",
        "Saving Project"}
    # there's also "COMPILATION STARTED" but the finish gives us the time

    home = str(Path.home())

    filename = "/" + home + "/Library/Logs/IdeaIC2019.2/idea.log"
    result = scrape(filename)
    print(result)
    print(list(result))
