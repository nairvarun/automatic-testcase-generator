#!/bin/bash

# TODO: check if all prev cmds ran successfully
gcc -O0 -fdump-tree-cfg-graph $1
dot -Tpng *$1.*.cfg.dot -o $1.cfg.png
grep -oP '^;; .* succs { .* }$' *$1.*.cfg > $1.cfg
python3 parse-cfg.py $1.cfg

# e=$(grep -oP '^;; .* succs { \K.*(?= }$)' *$1.*.cfg | tr '\n' ' ' | wc -w)
# a=$(grep "^;; .* succs { .* }$" *$1.*.cfg | wc -l)
# n=$((a+1))
# echo $e
# echo $n
# echo $(($e-$n+2))
    