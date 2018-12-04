from sh import *
import os
import getpass

def createKey():
    ssh_pass = getpass.getpass("Enter a password for your github ssh key")
    email = "\"coding.aaronp@gmail.com\""
    keypath = "/root/.ssh/mykey_rsa"
    sudo("ssh-keygen -t rsa -b 4096 -C %s -f %s -P \"%s\"" % (email, keypath, ssh_pass))
    print("")
    sudo("cat %s.pub" % (keypath))
    print("")
    print("Now go to https://github.com/settings/ssh/new and create a key with ^^^")
    print("")
    raw_input("Press enter when done")

def addLine(ln):
    sudo("echo '%s' >> ~/.ssh/config" % (ln))

def configure():
    addLine("host github.com")
    addLine("  HostName github.com")
    addLine("  IdentityFile ~/.ssh/mykey_rsa")
    addLine("  User git")
    sudo("eval `ssh-agent -s`")
    sudo("ssh-add -k ~/.ssh/mykey_rsa")

def getRepo(data):
    createKey()
    configure()

    title = data["title"]
    
    target = "/root/crucible"
    if not os.path.isdir(target):
        sudo("git clone git@github.com:aaron-price/crucible.git " + target)

    target = "/root/" + title
    if not os.path.isdir(target):
        sudo("mkdir " + target)

    target = "/root/%s/db" % (title)
    if not os.path.isdir(target):
        sudo("cp -a /root/crucible/db " + target)
        
    target = "/root/%s/server" % (title)
    if not os.path.isdir():
        sudo("cp -a /root/crucible/server " + target)
        
    target = "/root/%s/web" % (title)
    if not os.path.isdir():
        sudo("cp -a /root/crucible/web " + target)
