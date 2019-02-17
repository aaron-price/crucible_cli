from sh import *
import ui

def setupArango():
    sh("cd /etc/yum.repos.d/")
    sh("curl -OL https://download.arangodb.com/arangodb34/RPM/arangodb.repo")
    y("arangodb3-3.4.2-1")
    y("arangodb3-debuginfo-3.4.2-1")
