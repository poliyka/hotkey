import subprocess


def setup():
    cmd = "pip install pillow pynput win32gui"
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    setup()
    print("All work setup!")
