import subprocess 
import random
import string
from distutils.spawn import find_executable

def sh(s):
    print("==========")
    print(s)
    print("")
    subprocess.call(s, shell=True)
    print("==========")

sudo = lambda s: sh("sudo " + s)
y = lambda pkg: sudo("yum install -y " + pkg)
wget = lambda url: sudo("wget " + url)
curl = lambda url: sudo("curl " + url)
echo = lambda s: sudo("echo " + s)
rm = lambda s: sudo("rm -rf " + s)
ctl = lambda s: sudo("systemctl " + s)
update = lambda: sudo("yum update")

def cp(fr, to, r=False):
    if r == True:
        sudo("cp -r %s %s" % (fr, to))
    else:
        sudo("cp %s %s" % (fr, to))

def addPath(p):
    sudo("echo 'export PATH=\"$PATH:%s\"' >> /root/bash_config/paths.sh" % (p))
    sh("source /root/.bash_profile")

def wgetAs(url, filename):
    wget("-O %s %s" % (filename, url))

def rpm(url):
    wgetAs(url, "installer.rpm")
    sudo("rpm -Uvh installer.rpm")
    rm("installer.rpm")

def isInstalled(tool):
    return not find_executable(tool) == None

def replaceLine(filename, key, new_value, delimiter = ":"):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    if delimiter:
        for i, line in enumerate(lines):
            if line.split(delimiter)[0].strip(' \n') == key:
                lines[i] = key + delimiter + ' ' + new_value + '\n'
    else:
        for i, line in enumerate(lines):
            if key in line.split(" "):
                lines[i] = new_value + '\n'
    f = open(filename, "w")
    f.write("".join(lines))
    f.close()

def genpass(size=512, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))
