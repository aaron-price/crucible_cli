from sh import *
import ui

def addVariables():
    ip = shv('hostname -I').split()[0]
    secret = shv('cd /root/app/crucible/server && echo $(mix phx.gen.secret)')
    addPathVar('PROJECT_IP', ip)
    addPathVar('CRUCIBLE_SECRET_KEY_BASE', secret, True)
    
def npmInstallAt(p):
    sh("cd " + p + " && npm i")

def installDeps():
    crucible_path = "/root/app/crucible"
    server_path = crucible_path + "/server"
    web_path = crucible_path + "/web"
    cljs_path = crucible_path + "/web/fe"
    db_path = crucible_path + "/db"
    
    sh("git clone https://github.com/aaron-price/crucible.git /root/crucible")
    sh("cd /root/crucible/server && mix deps.get")
    npmInstallAt(web_path)
    npmInstallAt(cljs_path)
    npmInstallAt(db_path)

def runApp():
    sh("cd /root/app/crucible/server && mix phx.server")

def setupApp():
    installDeps()
    addVariables()
    runApp()
