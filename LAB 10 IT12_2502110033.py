IT12: Rough cut - Fix Yesterday's Gaps
To clear the "Handover Test" gaps, address relative paths and exception handling in your Python code.

Relative Paths: Replace hardcoded absolute paths with dynamic relative paths using os or pathlib so the code works on any machine.
import os

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the relative path to the data file
file_path = os.path.join(base_dir, '..', 'data', 'input_file.csv')
Remove Bare Exceptions & Tracebacks: Replace bare except: blocks with specific exception handling that returns a clean message to the user rather than a crash traceback.
try:
    with open(file_path, 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("Error: The required input file was not found in the 'data/' directory.")
except ValueError as ve:
    print(f"Error: Invalid data format encountered. Details: {ve}")
# Do NOT use a bare 'except:' here
