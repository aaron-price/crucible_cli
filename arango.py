from sh import *
import ui

def setupArango():
    sh("cd /etc/yum.repos.d/ && curl -OL https://download.arangodb.com/arangodb34/RPM/arangodb.repo")
    y("arangodb3")
    y("arangodb3-debuginfo")
    print "Here, have a password"
    print genpass()
    sudo("arango-secure-installation")
