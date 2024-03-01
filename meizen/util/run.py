import subprocess


def run(path: str):
    command = ["python", path]
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    output = result.stdout
    err = result.stderr
    print("コマンドを実行: " + str(command))
    print(output)
    print(err)


def run_args(path: str, args: list[str]):
    command = ["python", path]
    command += args
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    output = result.stdout
    err = result.stderr
    print("コマンドを実行: " + str(command))
    print(output)
    print(err)
