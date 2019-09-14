from pathlib import Path


def scrape(filename):
    # tag (INFO, etc)
    # date and time
    # kind of event
    # text at the end
    # dictionary
    f = open(filename, "r")
    print(f)
    line = f.readline()
    while line:
        for keyword in keywords:
            if keyword in line:
                line = line.strip("\n")
                line_parts_spaces = line.split(" ")
                line_parts_spaces = [elt for elt in line_parts_spaces if elt != ""]
                date = line_parts_spaces[0]
                time = line_parts_spaces[1]
                tag = line_parts_spaces[3] if line_parts_spaces[3].isalpha() else line_parts_spaces[4]
                print(line_parts_spaces)
                event_kind = keyword

                line_parts_hyphens = line.split("-")
                line_parts_hyphens = [elt for elt in line_parts_hyphens if elt != "" and elt != " "]
                print(line_parts_hyphens)
                message = line_parts_hyphens[-1]

                line_info = {"TAG" : tag,
                    "DATE" : date,
                    "TIME" : time,
                    "EVENT_KIND" : event_kind,
                    "MESSAGE" : message}

                yield line_info
        line = f.readline()


if __name__ == '__main__':
    keywords = { "IDE STARTED",
        "IDE SHUTDOWN",
        "COMPILATION STARTED",
        "COMPILATION FINISHED",
        "Saving Project" #,
        #"GitHandler"
        }
        # if it contains githandler, must also contain commit

        # text at the end
    # there's also "COMPILATION STARTED" but the finish gives us the time

    home = str(Path.home())

    filename = "/" + home + "/Library/Logs/IdeaIC2019.2/idea.log"
    result = scrape(filename)
    print(result)
    print(list(result))
