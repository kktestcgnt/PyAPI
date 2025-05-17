'''
import paramiko
import platform
import subprocess

class Network (object):

    def __init__(self):
        self.AP_IP = ""

    def reachability_test(self, AP):
        self.AP_IP = AP
        if platform.system() == 'Windows':
            print(platform.system())
            while True:
                test = ('ping {} -n 1'.format(AP))
                process = subprocess.Popen(test, shell=True, stdout=subprocess.PIPE)
                # give it time to respond
                process.wait()
                # optional check (0 --> success)
                print(process.returncode)
                if process.returncode != 0:
                    print(".....Waiting for reply from AP :", AP)
                    continue
                else:
                    print('Got ICMP response from AP :', AP)
                    time.sleep(5)
                    break
        elif platform.system() == 'Linux':
            print(platform.system())
            while True:
                test = ('ping {} -c 1'.format(AP))
                process = subprocess.Popen(test, shell=True, stdout=subprocess.PIPE)
                # give it time to respond
                process.wait()
                # optional check (0 --> success)
                print process.returncode
                if process.returncode != 0:
                    print ".....Waiting for reply from AP :", AP
                    continue
                else:
                    print 'Got ICMP response from AP :', AP
                    time.sleep(5)
                    break


    def wait_for_ssh_to_be_ready(self, AP_IP, port, timeout, retry_interval):
        self.AP_IP = AP_IP
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        retry_interval = float(retry_interval)
        timeout = int(timeout)
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            time.sleep(retry_interval)
            try:
                client.connect(AP_IP, int(port), allow_agent=False, look_for_keys=False)
            except paramiko.ssh_exception.SSHException as e:
                # socket is open, but not SSH service responded
                if e.message == 'Error reading SSH protocol banner':
                    print(e)
                    continue
                print('SSH transport is available!')
                break
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print('SSH transport is not ready...')
                continue


class SSHClient:
    @staticmethod
    def ssh_client():

        # Connection details
        hostname = "your.server.ip.or.hostname"  # e.g., "192.168.1.100"
        port = 22  # default SSH port
        username = "your_username"
        password = "your_password"

        # Create an SSH client
        client = paramiko.SSHClient()

        # Automatically add unknown host keys (not secure for production)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the server
            print(f"Connecting to {hostname}...")
            client.connect(hostname, port, username, password)
            print("Connected!")

            # Run a command (you can change this to anything, like 'ls', 'df -h', etc.)
            command = "uname -a"
            stdin, stdout, stderr = client.exec_command(command)

            # Print the output
            print("Command Output:")
            print(stdout.read().decode())

            # Print any errors
            err = stderr.read().decode()
            if err:
                print("Error:")
                print(err)

        except paramiko.AuthenticationException:
            print("Authentication failed, check your username/password.")
        except paramiko.SSHException as e:
            print(f"SSH error: {e}")
        except Exception as e:
            print(f"Some error occurred: {e}")
        finally:
            # Always close the connection
            client.close()
            print("Connection closed.")
'''
