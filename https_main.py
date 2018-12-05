#!/usr/bin/python
from sh import *
import ui

if __name__ == "__main__":
    domain = ui.getDomain()
    title = ui.getTitle()
    default_conf = "/etc/nginx/nginx.conf"
    crucible_conf = "/root/crucible_cli/files/nginx/HTTPSnginx.conf"
    rm(default_conf)
    cp(crucible_conf, default_conf)
    replaceLine(default_conf, "server_name", "        server_name %s www.%s;" % (domain, domain), False)
    ctl("reload nginx")
    sudo("certbot --nginx -d %s -d www.%s" % (domain, domain))
    sudo("openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048")
    ctl("reload nginx")
    print("Now copy this line, and paste it after hitting enter:")
    print("15 3 * * * /usr/bin/certbot renew --quiet")
    sudo("crontab -e")
    print("Ok, you're done!")
