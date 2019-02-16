from sh import *
import ui

def setupNode():
    sudo("curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -")
    y("nodejs")
