import subprocess
import platform
import re

# Prompt for user input
dst_ip = input(f"Please enter an IP address you would like to ping: ")
print()

# Check for OS (Windows or Linux) to run the proper command
if platform.system().lower() == "windows":
    command = ["ping", "-n", "4", dst_ip]  # Ping 4 times, Windows
    success_pattern = re.compile(r"Reply from")  # Windows success pattern
else:
    command = ["ping", "-c", "4", dst_ip]  # Ping 4 times, Linux
    success_pattern = re.compile(r"bytes from")  # Linux success pattern

# Run the ping command once and capture output
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = result.stdout.decode(errors="ignore")  # Decode output safely

# Process each line of output to check success/failure per ping
ping_count = 0  # Counter for actual ping responses
for line in output.split("\n"):
    if success_pattern.search(line):  # If the line matches a successful ping
        ping_count += 1
        print(f"Ping {ping_count}: Successful! ✅")
    elif "Request timed out" in line or "100% packet loss" in line or "Destination Host Unreachable" in line:
        ping_count += 1
        print(f"Ping {ping_count}: Failed ❌")

# Print the actual ping command output
print("\nFull ping output:\n" + "-" * 50)
print(output)
print("-" * 50)
