from sh import *
import ui

def setupJulia():
    sudo("yum-config-manager --add-repo https://copr.fedorainfracloud.org/coprs/nalimilan/julia/repo/epel-7/nalimilan-julia-epel-7.repo")
    y("julia")

