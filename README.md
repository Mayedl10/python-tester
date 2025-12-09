# PyTest

#### Main points:
- Evaluate if a student's script is implemented correctly
- Exercises stored in json format
- 2 Modes:
  - consoleIO mode
    - a specific input is meant to lead to a specific output - done via `python3 main.py > output.txt < input.txt`
  - modular mode
    - a helper script (.py) imports a function/class/other and tests it

#### Arguments

- `pytest -unpack tasks.json` - unpacks/prepares a set of tasks, stored in .json
- `pytest -test main.py exampleTest` - examines main.py according to test with label "exampleTest"
- `pytest -generate tasks` - takes a folder and converts it to a .json task set/sheet