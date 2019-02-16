function sourceAllMySettings (){
    for i in `find ~/bash_config -type f -not -name "*.swp"`; do
        . $i
    done;
}

sourceAllMySettings
