import logging


class LogApplication(object):
    file_name = "lib/log_file.log"
    logging.basicConfig(filename=file_name, level=logging.INFO, format='%(asctime)s: %(message)s')
    logger = logging.getLogger(__name__)

    def write_log_message(self, log_message):
        """
        Write a log in log file
        """
        self.logger.info("LOG MSG: " + log_message)
        return "Log message is wrote successfully"

    def write_log_message_with_class_name(self, log_message):
        """
        Write a log in log file with class name
        """
        self.logger.info("LOG MSG: "+str(log_message) + " CLASS NAME: " + str(self.__class__.__name__))
        return "Log message with class name wrote successfully"

    def read_log_message(self):
        """
        Read log file and display data
        """
        log_read = open(self.file_name, "r")
        logs = log_read.read().split("\n")
        log_read.close()
        log_msg = []
        for i in logs:
            if "LOG MSG: " in i:
                log_msg.append(i)
        return log_msg

    def read_log_messages_with_class_name_only(self):
        log_read = open(self.file_name, "r")
        logs = log_read.read().split("\n")
        log_read.close()
        log_msg = []
        logs.pop(len(logs)-1)
        for i in logs:
            if "LogApplication" in i:
                log_msg.append(i)
        return log_msg


if __name__ == "__main__":
    logapp = LogApplication()
    logapp.write_log_message("Testing log message")
    logapp.write_log_message_with_class_name("Testing log message with class name")
    log_messages = logapp.read_log_message()
    print("Read all log messages\n", log_messages)
    log_messages = logapp.read_log_messages_with_class_name_only()
    print("Read only log messages with class name\n", log_messages)
