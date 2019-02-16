# kill orphaned processes.
# What would be a better name for something that kills 3 orphans...
function snicket() {
    kill -9 $( ps -A | grep java | awk '{print $1}' )
    kill -9 $( ps -A | grep node | awk '{print $1}' )
    kill -9 $( ps -A | grep julia | awk '{print $1}' )
}
function config() {
    case $1 in
        bash)
            cd ~/bash_config; 
            vim;;
        git) vim ~/.gitconfig;;
        # powerline) vim ~/.config/powerline-shell/config.json;;
        vim) 
            cd ~/.vim; 
            vim;;
        *) print_options "bash" "git" "powerline" "vim";;
    esac
}

function crucible() {
    rebuild crucible;
    /root/crucible/ops/cli/crucible --env=prod;
}

function rebuild() {
    case $1 in
        crucible) 
            path=$( pwd );
            cd /root/crucible/ops/cli;
            mix escript.build;
            cd $path;;
        *) print_options "crucible";;
    esac
}

function start() {
    case $1 in
        nginx) systemctl start nginx;;
        arangodb) systemctl start arangodb3;;
        *) print_options "nginx arangodb";; 
    esac
}
function stop() {
    case $1 in
        nginx) systemctl stop nginx;;
        arangodb) systemctl stop arangodb3;;
        *) print_options "nginx arangodb";; 
    esac
}
function update() {
    case $1 in
        arangodb)
            foxx upgrade --database Crucible --password /gql /root/Crucible/db;;
        secrets)
            echo "export ${2^^}_SECRET_KEY_BASE=\"$(mix phx.gen.secret)\"" >> /root/bash_config/paths.sh;;
        *) print_options "arangodb secrets(Name)";;
    esac
}

function restart() {
    case $1 in
        nginx) systemctl restart nginx;;
        arangodb) systemctl restart arangodb3;;
        *) print_options "nginx arangodb";; 
    esac
}

function print_options() {
    for option in "$@"
    do
        :
        echo "- $option";
    done
}

function print_commands() {
    for keyword in "$@"
    do
        :
        echo "~~~$keyword~~~";
        $keyword;
        echo "";
    done
}
function commands() {
    echo "###########";
    echo "# config  #";
    echo "###########";
    
    print_commands config
}
