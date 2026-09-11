import sys
import subprocess

print("Python version:", sys.version)

print("Python Libraries Installed:")

subprocess.run(["pip", "list"])