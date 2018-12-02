from sh import *

cli_files = "/root/crucible_cli/files"

def setupBash():
    rm("~/.bash_profile")
    cp(cli_files + "/bash_profile.sh", "~/.bash_profile")
    cp(cli_files + "/bash_config", "~/bash_config", True)
    cp(cli_files + "/vim", "~/.vim", True)
    sh("source ~/.bash_profile")

    update()
    y("wget git unzip epel-release nginx")
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
    wget("https://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm")
    erl_name = "erlang-solutions-1.0-1.noarch.rpm"
    erl_url = "https://packages.erlang-solutions.com/" + erl_name
    sudo("rpm -Uvh " + erl_name)
    update()
    y("erlang inotify-tools")

    # Elixir
    ex_path = "/usr/bin/elixir"
    ex_url = "https://github.com/elixir-lang/elixir/releases/download/v1.7.4/Precompiled.zip"
    ex_zip = ex_path + "/Precompiled.zip"
    wget(ex_url + " " + ex_zip)
    sudo("unzip " + ex_zip)

    addPath(ex_path + "/bin")
    rm(ex_zip)

def setupCLJS():
    cljs_installer = "linux-install-1.9.0.397.sh"
    cljs_url = "https://download.clojure.org/install/" + cljs_installer
    curl("-O " + cljs_url)
    sudo("chmod +x " + cljs_installer)
    sudo("./" + cljs_installer)

    # lein
    local_lein = "/usr/local/bin/lein"
    wget("https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein " + local_lein)
    sudo("chmod a+x " + local_lein)
    
def setupNode():
    curl("-sL https://rpm.nodesource.com/setup_10.x | sudo bash -")
    update()
    y("nodejs build-essential")
    sudo("npm i -g bower")

def setupArango():
    sudo("npm i -g webpack foxx-cli")
    curl("-OL https://download.arangodb.com/arangodb33/CentOS_7/arangodb.repo /etc/yum.repos.d/arangodb.repo")
    y("arangodb3-3.3.19")
    y("arangodb3-debuginfo-3.3.19")

def installAll():
    setupBash()
    setupElixir()
    setupNode()
    setupCLJS()
    setupArango()
