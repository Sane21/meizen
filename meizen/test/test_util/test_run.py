from meizen.util.run import run, run_args


def test_run():
    path = "C:/Users/readb/pycharm/meizen/meizen/dncl/sample/"
    path += "sample.py"
    run(path=path)


def test_run_args():
    path = "C:/Users/readb/pycharm/meizen/meizen/dncl/sample/"
    path += "sample.py"
    args = [""]
    run_args(path=path, args=args)


test_run()
