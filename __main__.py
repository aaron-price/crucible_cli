#!/usr/bin/python
import ui
import install

if __name__ == "__main__":
    data = ui.getData()
    install.installAll()
    # Setup DB
    # Setup server
    # Setup web frontend
