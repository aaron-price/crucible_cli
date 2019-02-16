import textwrap
# Collect all user input in this module

# multipleChoice("""
# What would you like to do?
#
# 1. Generate an ssh key
# 2. Set up bash/vim
# """, {
#     "1": sshGen,
#     "2": bashSetup
# })
def multipleChoice(opt_str, dic):
    inp = raw_input(textwrap.dedent(opt_str))
    switcher = dic
    func = switcher.get(inp)
    return func()

def getTitle():
    defaultname = "Chimera"
    name = raw_input("Name your app (" + defaultname + "): ")
    return name if name != "" else defaultname

def getData():
    title = getTitle()
    ip = raw_input("What's the public ip of this droplet? ")
    return {
        "title": title,
        "path": "/root/" + title,
        "title_upper": title.upper(),
        "title_lower": title.lower(),
        "ip": ip
    }

def getDomain():
    return raw_input("Domain name (e.g. 'crucible.com'): ")
