#!/bin/bash

#set -xe

SOURCE_PATH="src/*.java"
CLASS_PATH="cls"

MOD_PATH="--module-path ${JAVA_FX_PATH}" 
MOD_OPT="--add-modules javafx.controls"

javac ${MOD_PATH} ${MOD_OPT} -d ${CLASS_PATH} ${SOURCE_PATH}

if ! [ -z $1 ];then
    if [ "$1" = 'r' ]; then
        if ! [ -z $2 ]; then
            java ${MOD_PATH} ${MOD_OPT} --enable-native-access=javafx.graphics -cp "${CLASS_PATH}" $2
            else
                echo "Insert name of the class you want to run"        
        fi

        else
            echo "Use argument flag 'r'"
    fi

fi
