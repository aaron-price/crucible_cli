from sh import *
import os
import getpass

def setupDB(data):
    title = data["title"]
    path = "/root/" + title + "/db"
    oldpwd = os.getcwd()
    os.chdir(path)
    sh("npm i")
    os.chdir(oldpwd)

    pswd = getpass.getpass("Password for database root user: ")
    sh("printf 'db._createDatabase(\"%s\")' | arangosh --server.password %s" % (title, pswd))
    sh("foxx install /gql %s --database=%s --username=root -v --setup --password" % (path, title))
