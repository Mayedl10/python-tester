# PyTest

#### Main points:
- Evaluate if a student's script is implemented correctly
- Exercises stored in json format
- 2 Modes:
  - consoleIO mode (1)
    - a specific input is meant to lead to a specific output
  - modular mode (2)
    - a helper script (python) imports a function/class/other and tests it

#### Usage

Parameters are passed without file extensions (assumes .py and .json)

`pytest [test] [script] [task#]`
- `test` is a valid test package in json format
- `script` is a python script
- `task#` is the task identifier within the package

To test the provided example, run `./pytest.py ./examples/example_package ./examples/example 0`

#### Package format

An example for a valid test format:
```js
{
    "tasks": [
        {
            "label":0,
            "description":"test number one",
            "tests":[
                {
                    "mode":1,
                    "input":"abc",
                    "output":"b",
                    "hidden":false,
                    "timeout":5
                },
                {
                    "mode":2,
                    "helper":"from test import foo\nfoo(\"cde\")",
                    "input":"",
                    "output":"d",
                    "hidden":true,
                    "timeout":5
                }
            ]
        }
    ]
}
```