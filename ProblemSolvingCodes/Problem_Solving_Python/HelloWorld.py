# Method 1
print("Hello World")

# Method 2
import sys
sys.stdout.write("Hello World\n")

# Method 3 # os.write() function to write directly to the file descriptor 1
import os
os.write(1, b"Hello World\n")

# Method 4
import subprocess
subprocess.run("echo hello world", shell=True)
