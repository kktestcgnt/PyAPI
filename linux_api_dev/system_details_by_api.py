import flask
import socket


obj_flask = flask.Flask(__name__)
obj_flask.config["DEBUG"] = True


@obj_flask.route("/cmd_system_ip", methods=["GET"])
def system_ip():
    system_details = {}
    system_details['hostname'] = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    system_details['ip_address'] = s.getsockname()[0]
    s.close()
    return system_details


obj_flask.run(host='192.168.29.112', port=9966)
