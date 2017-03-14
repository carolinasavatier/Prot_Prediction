f=$1
cat $f | xargs -P 4 -I[] ./psi-blast.sh []
