#!/bin/bash

# Check if a version was provided
if [ -z "$1" ]
then
    echo "Please provide a version. Usage: ./script.sh 4.9.y"
    exit 1
fi

# Get the version from the command line argument
version=$1

THIS_DIR=`pwd`
cd seL4-CAmkES-L4v-dockerfiles &&
make EXEC='bash -c "\
    rm -rf /host/build-'$version' || { echo '\''Failed to delete /host/build-'$version''\''; exit 1; }; \
    mkdir /host/build-'$version' || { echo '\''Failed to create /host/build-'$version''\''; exit 1; }; \
    cd /host/build-'$version' || { echo '\''Failed to change to /host/build-'$version' directory'\''; exit 1; }; \
    ../init-build.sh -DCAMKES_VM_APP=attarch-'$version' -DPLATFORM=qemu-arm-virt && \
    ninja"' user HOST_DIR=$THIS_DIR

