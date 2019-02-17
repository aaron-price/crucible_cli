from sh import *
import ui

def setupArango():
    sh("cd /etc/yum.repos.d/ && curl -OL https://download.arangodb.com/arangodb34/RPM/arangodb.repo")
    y("arangodb3")
    y("arangodb3-debuginfo")
    print "Here, have a password"
    pswd = genpass()
    print pswd
    sudo("arango-secure-installation")
    ctl("start arangodb")
    sh("printf 'db._createDatabase(\"main\")' | arangosh --server.password %s" % (pswd))
    sh("mkdir -p /root/app/arango/")
    sh("npm i -g foxx-cli")
    # @TODO
    # sh("foxx install /gql /root/app/arango --database=\"main\" --password /gql /root/app/arango")
