from sh import *
import ui

def setupHttps():
    cli_files = "/root/crucible_cli/resources"
    y("epel-release nginx")
    y("certbot-nginx")
    ctl("start nginx")
    ctl("enable nginx")
    rm("/etc/nginx/nginx.conf")

    # Setup plain http proxy as placeholder until domain set up.
    cp(cli_files + "/nginx/http/nginx.conf", "/etc/nginx/nginx.conf")
    ctl("restart nginx")
    sudo("setsebool -P httpd_can_network_connect 1")
    
    print("Set the NS records for the domain, plus two A record (www.domain.com and domain.com)")
    print("")
    print("Follow the steps here to the letter: ")
    print("https://linuxize.com/post/secure-nginx-with-let-s-encrypt-on-centos-7/")
    print("")
    print("Then add a couple lines inside your 'location / {}' block")
    print("https://github.com/socketio/socket.io/issues/1942#issuecomment-82352072")
    print("")
    print("And finally update the domain in ./server/config/prod.exs")
    print("")
    print("Some example files can be found in crucible_cli/files/nginx")
