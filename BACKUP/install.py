import os
from sh import *

cli_files = "/root/crucible_cli/files"

def setupBash():
    rm("~/.bash_profile")
    cp(cli_files + "/bash_profile.sh", "~/.bash_profile")
    cp(cli_files + "/bash_config", "~/bash_config", True)
    cp(cli_files + "/vim", "~/.vim", True)
    sh("source ~/.bash_profile")

    update()
    y("wget git unzip epel-release nginx vim")
    y("certbot-nginx")
    sudo("git config --global user.email \"coding.aaronp@gmail.com\"")
    sudo("git config --global user.name \"aaron-price\"")
    ctl("start nginx")
    ctl("enable nginx")
    rm("/etc/nginx/nginx.conf")
    cp(cli_files + "/nginx/HTTPnginx.conf", "/etc/nginx/nginx.conf")
    ctl("restart nginx")
    sudo("setsebool -P httpd_can_network_connect 1")

def setupElixir():
    # fulfill some prerequisites
    update()
    y("gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf")
    y("java-1.8.0-openjdk-devel wxBase.x86_64")

    # Erlang
    # NEVER USE RABBITMQ! 
    # They remove vital libs from erlang, which makes elixir impossible to install.
    # erl_url = "https://github.com/rabbitmq/erlang-rpm/releases/download/v21.1.4/erlang-21.1.4-1.el7.centos.x86_64.rpm"
    
    erl_url = "http://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm"
    rpm(erl_url)
    update()
    y("esl-erlang inotify-tools")

    # Elixir
    sudo("git clone --single-branch --branch v1.8 https://github.com/elixir-lang/elixir.git /opt/elixir")
    sudo("cd /opt/elixir")
    sudo("make clean test")
    sudo("sudo ln -s /opt/elixir/bin/iex /usr/local/bin/iex")
    sudo("sudo ln -s /opt/elixir/bin/mix /usr/local/bin/mix")
    sudo("sudo ln -s /opt/elixir/bin/elixir /usr/local/bin/elixir")
    sudo("sudo ln -s /opt/elixir/bin/elixirc /usr/local/bin/elixirc")

def setupCLJS():
    cljs_installer = "linux-install-1.9.0.397.sh"
    cljs_url = "https://download.clojure.org/install/" + cljs_installer
    curl("-O " + cljs_url)
    sudo("chmod +x " + cljs_installer)
    sudo("./" + cljs_installer)
    rm(cljs_installer)

    # lein
    local_lein = "/usr/local/bin/lein"
    wgetAs("https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein", local_lein)
    addPath(local_lein)
    sudo("chmod a+x " + local_lein)
    sh("lein")
    
def setupNode():
    curl("-sL https://rpm.nodesource.com/setup_10.x | sudo bash -")
    update()
    y("nodejs build-essential")
    sudo("npm i -g bower")

def setupArango():
    # Arango
    rpm("https://download.arangodb.com/arangodb33/CentOS_7/x86_64/arangodb3-3.3.19-1.x86_64.rpm")

    # Arango Client
    rpm("https://download.arangodb.com/arangodb33/CentOS_7/x86_64/arangodb3-client-3.3.19-1.x86_64.rpm")

    # Arango debug info
    rpm("https://download.arangodb.com/arangodb33/CentOS_7/x86_64/arangodb3-debuginfo-3.3.19-1.x86_64.rpm")

    update()
    sudo("npm i -g webpack foxx-cli")
    sudo("export GLIBCXX_FORCE_NEW=1")
    sudo("bash -c \"echo madvise > /sys/kernel/mm/transparent_hugepage/enabled\"")
    sudo("bash -c \"echo madvise > /sys/kernel/mm/transparent_hugepage/defrag\"")
    print("=== SETTING UP ARANGODB ===")
    sudo("arango-secure-installation")
    ctl("start arangodb3")



def installAll():
    if not isInstalled("nginx"):
        setupBash()
    if not isInstalled("elixir"):
        setupElixir()
    if not isInstalled("node"):
        setupNode()
    if not isInstalled("clj"):
        setupCLJS()
    if not isInstalled("arangodb"):
        setupArango()
    sh("source ~/.bash_profile")
