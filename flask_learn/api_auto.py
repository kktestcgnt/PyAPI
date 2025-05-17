import requests
import json
import time

server_ip = '192.168.29.112'
new_ssid_name = 'new_ssid'
new_ssid_temp = 'new_ssid_template'


url_login = 'http://192.168.29.112:9966/cmd_system_ip'

status_login = requests.get(url_login)
response_status = status_login.status_code
print(response_status)
# print("Login API CALL : ", status_login)
print("Login API CALL : ", status_login.text)
data = json.loads(status_login.text)
print(type(status_login.text))
print(data, type(data))
# print("Login API CALL : ", status_login.r)
# print(status_login.cookies)
# print()
# print("LOGIN SUCCESSFUL")
