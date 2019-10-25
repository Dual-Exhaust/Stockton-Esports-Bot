# All this does is write a new line to the log.txt file that contains the log event we pass as parameters
class Logger:
    def __init__(self):
        pass

    @staticmethod
    def log_event(title, description, time):
        log = str("<" + str(title) + ">" + "<" + str(description) + ">" + "<" + str(time) + ">")

        with open(r"log.txt", "a") as doc:
            doc.write(log + "\n")
