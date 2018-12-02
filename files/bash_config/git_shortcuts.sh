#### GIT SHORTCUTS
# e.g. cm "Commit message here"
function cm() {
  git add -A
  git commit -m "$@"
}
function co() {
  git checkout "$@"
}

# pushes to remote, current branch
function pu() {
  git push -u origin HEAD
}

