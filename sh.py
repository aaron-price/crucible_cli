import subprocess 

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
