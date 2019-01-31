from sh import *
import os

def setupServer(data):
    title = data["title"]
    upper = data["title_upper"]
    server_path = "/root/" + title + "/server"
    config_path = server_path + "/config/config.exs"

    # Set the IP
    ip = data["ip"]
    replaceLine(config_path, "web_url", "System.get_env(\"PROJECT_IP\"),")
    sudo("echo export PROJECT_IP=\"%s\" >> ~/.bash_profile" % (ip))
    
    # Set db url
    db_url = "\"http://localhost:8529/_db/" + title + "/gql\","
    replaceLine(config_path, "db_url", db_url)

    # Set secret key base
    secret = title + "_SECRET_KEY_BASE"
    sudo("echo export %s=\"$(mix phx.gen.secret 90)\" >> ~/.bash_profile" % (secret))
    replaceLine(config_path, "secret_key_base", "System.get_env(\"%s\")," % (secret))
    
    # Prepare elixir
    os.chdir(server_path)
    rm("mix.lock")
    sh("mix deps.get")
