from sh import *
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
    sudo("git clone git@github.com:aaron-price/crucible.git /root/crucible")
    sudo("mkdir /root/ " + title)
    sudo("cp -a /root/crucible/db /root/" + title + "/db/")
    sudo("cp -a /root/crucible/server /root/" + title + "/server/")
    sudo("cp -a /root/crucible/web /root/" + title + "/web/")
