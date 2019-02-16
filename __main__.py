#!/usr/bin/python
from ui import multipleChoice
from ssh_gen import sshGen
from bash import bashSetup

if __name__ == "__main__":
    goal = multipleChoice("""
    What would you like to do?

    1. Generate an ssh key
    2. Set up bash/vim
    """, {
        "1": sshGen,
        "2": bashSetup
    })
