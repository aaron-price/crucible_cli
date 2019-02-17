from sh import *
import ui

def setupElixir():
    update()
    y("gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf")
    y("java-1.8.0-openjdk-devel wxBase.x86_64")
    
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