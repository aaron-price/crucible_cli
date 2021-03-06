from sh import *

cli_files = "/root/crucible_cli/resources"

def bashSetup():
    rm("~/.bash_profile")
    cp(cli_files + "/.bash_profile", "~/.bash_profile")
    cp(cli_files + "/bash_config", "~/bash_config", True)
    sh("source ~/.bash_profile")
    update()
    y("wget unzip vim")
    sudo("git config --global user.email \"coding.aaronp@gmail.com\"")
    sudo("git config --global user.name \"aaron-price\"")

    # vimfiles are in a separate repo for convenience outside crucible.
    sudo("git clone https://github.com/aaron-price/vim.git ~/.vim")
    print("Bash and vim are all set up now!")

def add(str):
    sudo("echo '%s' >> /root/bash_config/commands.sh" % (str))

def customize(data):
    title = data["title"]
    add("function deploy() {")
    add("    rm -rf /root/%s/server/priv/static/js" % (title))
    add("    cd /root/%s/web;" % (title))
    add("    npm run deploy;")
    add("    cd /root/%s/server;" % (title))
    add("    MIX_ENV=prod mix release;")
    add("    _build/prod/rel/server/bin/server restart && echo \"Deployment Complete\" || _build/prod/rel/server/bin/server start;")
    add("}")

