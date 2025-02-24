import subprocess
import platform

# Prompt for user input
dst_ip = input(f"Please enter an IP address you would like to ping: ")
print()
# Check for OS (Windows or Linux) to run proper command
if platform.system().lower() == "windows":
    command = ["ping", "-n", "1", dst_ip] # Ping once, Windows
else:
    command = ["ping", "-c", "1", dst_ip] # Ping once, Linux
# Runs the 'ping' command
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture the output of ping command, in bytes.
# Then use .decode() to convert that output to a string. An error is otherwise thrown regarding 'bytes' output
if result.returncode == 0:
    print("Ping Successful!")
    print(result.stdout.decode(errors="ignore")) # Preventative measure taken in case there are errors in deconding
else:
    print("Ping Failed!")
    print(result.stdout.decode(errors="ignore")) # Still prints the stdout as a string as it still  contains useful info

