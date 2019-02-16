#!/usr/bin/python
import ui
import install
import getRepo
import db
import web
import server
import bash

if __name__ == "__main__":
    data = ui.getData()
    install.installAll()
    getRepo.getRepo(data)
    db.setupDB(data)
    web.setupWeb(data)
    server.setupServer(data)
    bash.customize(data)
    print("Now restart the shell (exit ; access %s)" % (data["title"]))
    print("And you can start the server with `cd %s/server && mix phx.server`" % (data["title"]))
