# Automatically use ssh keys
eval `ssh-agent -s` > out.log 2> out.log;
ssh-add -K ~/.ssh/something_rsa > out.log 2> out.log;

vim() {
    # osx users, use stty -g;
    local STTYOPTS="$(stty -g)";
    stty stop '' -ixoff;
    command vim "$@";
    stty "$STTYOPTS";
}
REACT_EDITOR=vim
