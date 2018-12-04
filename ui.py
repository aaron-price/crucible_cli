# Collect all user input in this module

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
