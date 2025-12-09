#!/usr/bin/python3

# This file handles the pytest console interface

from _pytest.src.testCode import *
import json
import sys
import os.path

def is_str_int(s: str) -> bool:
    """Return True if *s* represents an integer without a decimal point."""
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())

# check if the parameters are valid
if len(sys.argv) < 4:
    print("Please provide at least three arguments.\nUsage: pytest [test] [script] [task#] (without file extensions)")
    exit()

if not os.path.isfile(f"{sys.argv[1]}.json"):
    print("Please provide a valid json file (without the file extension) as the first parameter")
    exit()

if not os.path.isfile(f"{sys.argv[2]}.py"):
    print("Please provide a valid python file (without the file extension) as the second parameter")
    exit()

if not is_str_int(sys.argv[3]):
    print("Please provide an integer task identifier as the third parameter")
    exit()

with open(sys.argv[1]+".json", "r") as f:
    package = json.load(f)
f.close()
script = sys.argv[2]+".py"
identifier = int(sys.argv[3])

# execute tests matching identifier
for task in package["tasks"]:
    if (task["label"] == identifier):
        testTask(script, task)
        break
else:
    # invalid identifier
    print(f"No task with identifier {identifier} was found in package {sys.argv[1]}.json")