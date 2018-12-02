import subprocess 

sh = lambda s: subprocess.call(s, shell=True)
sudo = lambda s: sh("sudo " + s)
y = lambda pkg: sudo("yum install -y " + pkg)
wget = lambda url: sudo("wget " + url)
curl = lambda url: sudo("curl " + url)
echo = lambda s: sudo("echo " + s)
rm = lambda s: sudo("rm -rf " + s)
ctl = lambda s: sudo("systemctl " + s)

def cp(fr, to, r=False):
    if r == True:
        sudo("cp -r %s %s" % (fr, to))
    else:
        sudo("cp %s %s" % (fr, to))

def addPath(p):
    sudo("echo 'export PATH=\"$PATH:%s\"' >> /root/bash_config/paths.sh", % (p))
