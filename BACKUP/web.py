
from sh import *
import os

def setupWeb(data):
    title = data["title"]
    path = "/root/" + title + "/web"
    oldpwd = os.getcwd()
    os.chdir(path)
    sh("npm i")
    os.chdir(oldpwd)
