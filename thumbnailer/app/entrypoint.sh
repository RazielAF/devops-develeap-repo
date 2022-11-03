#!/bin/bash
pushd ..
echo $(pwd)
list=$(find pics/ -name "*")
dir=$(pwd)
popd
for file in $list
do
    ./thumbnail.sh -s=$1 $dir/$file
done