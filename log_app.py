from flask import Flask
from lib.log_application import LogApplication

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/write/log_msg/<message>", methods=['GET'])
def write_only_log_message(message):
    response = LogApplication().write_log_message(message)
    return {"response": response}


@app.route("/write/log_msg/cls_name/<message>", methods=['GET'])
def write_log_msg_with_cls_name(message):
    response = LogApplication().write_log_message_with_class_name(message)
    return {"response": response}


@app.route("/read/log_msg/", methods=['GET'])
def read_log_msg():
    response = LogApplication().read_log_message()
    return {"response": response}


@app.route("/read/log_msg/cls_name", methods=['GET'])
def read_log_msg_with_cls_name():
    response = LogApplication().read_log_messages_with_class_name_only()
    return {"response": response}


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
