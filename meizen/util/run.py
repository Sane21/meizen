import subprocess


def run(path: str):
    command = ["python", path]
    subprocess.run(command)
    print("コマンドを実行: " + str(command))


def run_args(path: str, args: list[str]):
    command = ["python", path]
    command += args
    subprocess.run(command)
    print("コマンドを実行: " + str(command))
