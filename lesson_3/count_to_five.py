import time

start_time = time.time()
timeout = 5

print("\nLet's count to 5 in 1 second increments...\n")
while time.time() - start_time < timeout:
    time.sleep(1)
    time_spent = time.time() - start_time
    clean_time = int(time_spent)
    print(f".....{clean_time}")

time_spent = time.time() - start_time
clean_time = int(time_spent)
print(f"\nTimes Up! Total Elapsed Time: {clean_time} Seconds")
print()

