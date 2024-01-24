import subprocess


def run(path: str):
    subprocess.run(["python", path])


def run_args(path: str, args: list[str]):
    command = ["python", path]
    command += args
    subprocess.run(command)
