#!/usr/bin/python
import ui
import install
import getRepo

if __name__ == "__main__":
    data = ui.getData()
    install.installAll()
    getRepo.getRepo(data)
    # Setup server
    # Setup web frontend
