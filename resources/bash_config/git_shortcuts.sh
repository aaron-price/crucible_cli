# e.g. cm "Commit message here"
function cm() {
  git add -A
  git commit -m "$@"
}

# co master
function co() {
  git checkout "$@"
}

# pushes to remote, current branch
function pu() {
  git push -u origin HEAD
}
