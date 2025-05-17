'''
import flask

obj_flask = flask.Flask(__name__)
obj_flask.config["DEBUG"] = True

x = 20


@obj_flask.route("/cmd_home", methods=["GET", "POST"])
def home():
    global x
    x = 210
    if x > 100:
        return f"Going to home: {x}", 202
    else:
        return f"Going to home: {x}", 304


@obj_flask.route("/cmd_clean", methods=["GET", "POST"])
def clean():
    global x
    x = 230
    if x > 100:
        return f"Clean Area: {x}", 202
    else:
        return f"Clean Area: {x}", 304


obj_flask.run(host='192.168.29.112', port=5000)
'''

import flask
import subprocess

obj_flask = flask.Flask(__name__)
obj_flask.config["DEBUG"] = True

x = 20


@obj_flask.route("/cmd_clean", methods=["GET", "POST"])
def clean():
    global x
    x = 240
    script_path = "/api_scripts/robot_home.sh"
    result = subprocess.run(['bash', script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Printing the script's output and error (if any)
    print("Output:", result.stdout.decode())



    if x > 100:
        return f"\"Output:\", {result.stdout.decode()}", 202
    else:
        return f"Going to home: {x}", 304


obj_flask.run(host='192.168.29.112', port=9966)
