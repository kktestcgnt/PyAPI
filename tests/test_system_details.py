import requests
import json
import socket
import pytest
import time

server_ip = '192.168.29.112'


def test_get_system_details():

    system_details = {}
    url_login = 'http://' + server_ip + ':9966/cmd_system_ip'

    status_login = json.loads(requests.get(url_login).text)
    system_details['hostname'] = status_login['hostname']
    system_details['ip_address'] = status_login['ip_address']
    status_code = requests.get(url_login).status_code
    system_details['api_status'] = status_code
    print(system_details)
    # return system_details


def test_post_data_details():
    url = 'http://' + server_ip + ':9966/cmd_update_file_in_linux'
    win_system_details = {}
    win_system_details['hostname'] = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    win_system_details['ip_address'] = s.getsockname()[0]
    s.close()
    # print(win_system_details)
    # win_system_details_json = json.dumps(win_system_details)
    print("win_system_details_json ::: ", type(win_system_details))
    response = requests.post(url, json=win_system_details)
    print(response.text)

