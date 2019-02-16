#!/usr/bin/python
from ui import multipleChoice
from ssh_gen import sshGen
from bash import bashSetup
from https import setupHttps
from node import setupNode

if __name__ == "__main__":
    goal = multipleChoice("""
    What would you like to do?

    1. Generate an ssh key
    2. Set up bash/vim
    3. Set up NGINX with https
    4. Install node & npm
    """, {
        "1": sshGen,
        "2": bashSetup,
        "3": setupHttps,
        "4": setupNode
    })
