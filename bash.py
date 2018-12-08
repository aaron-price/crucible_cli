from sh import *
def add(str):
    sudo("echo '%s' >> /root/bash_config/commands.sh" % (str))

def customize(data):
    title = data["title"]
    add("function deploy() {")
    add("    cd /root/%s/web;" % (title))
    add("    npm run deploy;")
    add("    cd /root/%s/server;" % (title))
    add("    MIX_ENV=prod mix release;")
    add("    _build/prod/rel/server/bin/server restart && echo \"Deployment Complete\" || _build/prod/rel/server/bin/server start;")
    add("}")

