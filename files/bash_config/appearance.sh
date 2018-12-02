end="\033[0m"
black="\033[0;30m"
blackb="\033[1;30m"
white="\033[0;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
green="\033[0;32m"
greenb="\033[1;32m"
yellow="\033[0;33m"
yellowb="\033[1;33m"
blue="\033[0;34m"
blueb="\033[1;34m"
purple="\033[0;35m"
purpleb="\033[1;35m"
lightblue="\033[0;36m"
lightblueb="\033[1;36m"

# colEcho $color text
function colEcho() {
    echo -e "${1}${2}${end}"
}
renderSpacer="......................."
renderPath="$(colEcho $yellow "\w")"
renderUser="$(colEcho $redb "\u@\h")"
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
#source /Library/Developer/CommandLineTools/usr/share/git-core/git-prompt.sh

# renderBranch="$(colEcho $green "\$(__git_ps1)")"
#export PS1="\n${renderSpacer}\n${renderPath}\n${renderUser}${renderBranch}: "
#function _update_ps1() {
#    PS1=$(powerline-shell $?)
#}

#if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
#    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
#fi
