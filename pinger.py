import subprocess
import time

def network_ping_test(ip_address, attempts, time_between_attempts=1):
    """pings an ip address"""

    # so we can control the time, use the -c 1 parsing to the ping command ourselves.
    shell_cmd = ["ping", "-c", "1", ip_address]

    # we will use subprocess to use terminal commands. 
    for i in range(attempts):
        run_command = subprocess.run(
            shell_cmd, 
            capture_output=True,
            text=True)
        print(f"attempt{i}: {run_command.stdout}" )

        if run_command.returncode == 0:
            print(f"attempt number: {i} -> command successful")
        else:   
            print("command failed")

        # control the attempts to ping.
        if time_between_attempts >= 1:
            time.sleep(time_between_attempts)
        else:
            print("the value of time_between_attempts must be greater than 1.")

def main():
    ip_address = "192.168.0.1"
    network_ping_test(ip_address, 1, 5)

main()
print(network_ping_test.__doc__)
    
