from sh import *
import getpass

def createKey():
    ssh_pass = getpass.getpass("Enter a password for your github ssh key")
    email = "\"coding.aaronp@gmail.com\""
    key_path = "/root/.ssh/mykey_rsa"
    sudo("ssh-keygen -t rsa -b 4096 -C %s -f %s -P \"%s\"" % (email, keypath, ssh_pass))
    print("")
    sudo("cat %s.pub" % (key_path))
    print("")
    print("Now go to https://github.com/settings/keys and create a new key with ^^^")
    input("Press enter when done")

def addLine(ln):
    sudo("echo %s >> ~/.ssh/config" % (ln))

def configure():
    addLine("host github.com")
    addLine("  HostName github.com")
    addLine("  IdentityFile ~/.ssh/mykey_rsa")
    addLine("  User git")
    sudo("eval `ssh-agent -s`")
    sudo("ssh-add -k ~/.ssh/mykey_rsa")

def getRepo():
    createKey()
    configure()
    sudo("git clone git@github.com:aaron-price/crucible.git")
