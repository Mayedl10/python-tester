#!/usr/bin/python3

# This file handles the pytest console interface

from _pytest.src.testCode import *
import json

with open("testpackage.json", "r") as f:
    data = json.load(f)
f.close()

testTask("test.py", data["tasks"][0])