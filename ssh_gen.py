from sh import genpass, sudo
from ui import multipleChoice

def sshGen():
    name = raw_input("name the key: ")
    print "Ok you're going to need to enter this path:"
    print "/Users/aaron/.ssh/" + name + "_rsa"
    print """
    Here, have a random password!
    %s

    """ %(genpass())

    target = multipleChoice("""
    What's the ssh target?

    1. digitalocean
    2. github
    """, {
        "1": lambda: sudo("ssh-keygen -t rsa"),
        "2": lambda: sudo("ssh-keygen -t rsa -b 4096 -C \"coding.aaronp@gmail.com\"")
    })
