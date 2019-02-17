from sh import *
import ui

def setupClojure():
    sh("curl -O https://download.clojure.org/install/linux-install-1.10.0.414.sh")
    sh("chmod +x linux-install-1.10.0.414.sh")
    sh("sudo ./linux-install-1.10.0.414.sh")
    sh("wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein")
    sudo("chmod +x lein")
    sudo("mv lein /usr/local/bin/lein")
    sh("lein")
