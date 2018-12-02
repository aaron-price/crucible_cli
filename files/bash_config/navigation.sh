# ls as soon as you cd.
function cl() {
  cd "$@" && ls -la;
}
