from sh import *
import os

def setupServer(data):
    title = data["title"]
    ip = data["ip"]
    upper = data["title_upper"]
    sudo("echo export %s_SECRET_KEY_BASE=$(mix phx.gen.secret 90) >> ~/.bash_profile" % (upper))
    sudo("echo export %s_IP=%s >> ~/.bash_profile" % (upper, ip))
    path = "/root/" + title + "/server"
    #oldpwd = os.getcwd()
    os.chdir(path)
    rm("mix.lock")
    sh("mix deps.get")

    # Endgame. This is the watch daemon.
    sh("mix phx.server")
