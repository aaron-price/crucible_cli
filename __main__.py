#!/usr/bin/python
from ui import multipleChoice
from ssh_gen import sshGen
from bash import bashSetup
from nginx import setupHttp, setupHttps
from node import setupNode
from elixir import setupElixir

if __name__ == "__main__":
    goal = multipleChoice("""
    What would you like to do?

    1. Generate an ssh key
    2. Set up bash/vim
    3. Set up NGINX
    4. Set up HTTPS (must do ^above^ first)
    5. Install node & npm
    6. Install erlang & elixir
    """, {
        "1": sshGen,
        "2": bashSetup,
        "3": setupHttp,
        "4": setupHttps,
        "5": setupNode,
        "6": setupElixir
    })
