from sh import *

def setupDB(data):
    sh("printf 'db._createDatabase(%s)' | arangosh --server.authentication true" % (data["title"]))
