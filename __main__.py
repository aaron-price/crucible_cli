#!/usr/bin/python
import ui
import install
import getRepo
import db
import web
import server

if __name__ == "__main__":
    data = ui.getData()
    install.installAll()
    getRepo.getRepo(data)
    db.setupDB(data)
    web.setupWeb(data)
    server.setupServer(data)
