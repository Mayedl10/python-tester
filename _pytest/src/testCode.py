import subprocess

TESTFILE = "./_pytest/live/test.py"
HELPERFILE = "./_pytest/live/helper.py"

def testTask(file:str, task:dict)->None:

    with open(file, "r") as f:
        code = f.read()
    f.close()

    with open(TESTFILE, "w") as f:
        f.write(code)
    f.close()

    results = []

    for i in range(len(task["tests"])):
        t = task["tests"][i]
        response = []

        if t["mode"] == 1:
            response = [testConsoleMode(file, t), t]

        elif t["mode"] == 2:
            response = [testModularMode(file, t), t]
        
        response.append(t["output"].strip() == response[0].stdout.strip() and response[0].stderr.strip() == "")
        results.append(response)

    printTestOutcome(results)



def testConsoleMode(file:str, test:dict)->subprocess.CompletedProcess:
    inp = test["input"]

    try:
        result = subprocess.run(
            ["python3", file],
            input=inp,
            capture_output=True,
            text=True,
            timeout=test["timeout"]
        )
    except subprocess.TimeoutExpired as exc:
        # The process was killed after the timeout.
        # exc.stdout and exc.stderr contain whatever was captured up to that point.
        result = subprocess.CompletedProcess(
            args=exc.cmd,
            returncode=1,
            stdout=exc.stdout or "",
            stderr=exc.stderr or f"Timed out after {test['timeout']} seconds\n"
        )

    return result


def testModularMode(file:str, test:dict)->subprocess.CompletedProcess:
   
    with open(HELPERFILE, "w") as f:
        f.write(test["helper"])
    f.close()

    inp = test["input"]

    try:
        result = subprocess.run(
            ["python3", HELPERFILE],
            input=inp,
            capture_output=True,
            text=True,
            timeout=test["timeout"]
        )
    except subprocess.TimeoutExpired as exc:
        # The process was killed after the timeout.
        # exc.stdout and exc.stderr contain whatever was captured up to that point.
        result = subprocess.CompletedProcess(
            args=exc.cmd,
            returncode=1,
            stdout=exc.stdout or "",
            stderr=exc.stderr or f"Timed out after {test['timeout']} seconds\n"
        )

    return result

def printTestOutcome(results:list)->None:
    score = 0
    for i in range(len(results)):
        r = results[i][0]
        t = results[i][1]
        s = results[i][2]
        
        print(f"--- Test {i+1} ---")
        
        if t["hidden"] == False:
            if results[i][1]["mode"] == 1:
                print(f"Input:\t\t{t['input']}")
                print(f"Expected:\t{t['output']}")
                print(f"Received:\t{r.stdout.strip()}")
                
                if s:
                    print("> Success <")
                    score += 1
                else:
                    print("> Failed <")
                    print(r.stderr, end="")
                
            if results[i][1]["mode"] == 2:
                print(f"Input handled by helper script")
                print(f"Expected:\t{t['output']}")
                print(f"Output:\t\t{r.stdout.strip()}")
                
                if s:
                    print("> Success <")
                    score += 1
                else:
                    print("> Failed <")
                    print(r.stderr, end="")

        else:
            if (s):
                score += 1
                print("Hidden test\n> Success <")
            else:
                print("Hidden test\n> Failed <")

        print()
    print(f"--- Summary ---\nPassed {score}/{len(results)} tests")
    