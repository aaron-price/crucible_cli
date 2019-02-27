from sh import *
import ui

def setupElixir():
    update()
    y("gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf wget unzip")
    y("java-1.8.0-openjdk-devel wxBase.x86_64")
    
    # Erlang
    erl_url = "http://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm"
    rpm(erl_url)
    update()
    y("esl-erlang inotify-tools")

    # Elixir
    sudo("sudo mkdir -p /opt/elixir")
    sudo("wget https://github.com/elixir-lang/elixir/releases/download/v1.8.1/Precompiled.zip")
    sudo("mv Precompiled.zip /tmp")
    sudo("unzip /tmp/Precompiled.zip -d /opt/elixir")
    #sh("for e in elixir elixirc iex mix; do sudo ln -s /opt/elixir/bin/${e} /usr/local/bin/${e}; done")
    sh("cd /root/")
    sh("mix local.hex")
    sh("mix archive.install hex phx_new 1.4.1")
