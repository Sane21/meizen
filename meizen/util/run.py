import subprocess


def run(path: str):
    command = ["python", path]
    output = subprocess.run(command, shell=False, capture_output=True, text=True).stdout
    print("コマンドを実行: " + str(command))
    print(output)


def run_args(path: str, args: list[str]):
    command = ["python", path]
    command += args
    output = subprocess.run(command, shell=False, capture_output=True, text=True).stdout
    print("コマンドを実行: " + str(command))
    print(output)
