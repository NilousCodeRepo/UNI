#!/bin/bash

#set -xe

if ! [ -z $1 ];then
    COMP_OPT="-Werror -g:none -Xlint"

    if [ "$1" = 'v' ];then
        COMP_OPT="-Werror -g:none -verbose -Xlint"
    fi
fi

SOURCE_PATH="src/*.java"
CLASS_PATH="cls"

MOD_PATH="--module-path ${JAVA_FX_PATH}" 
MOD_OPT="--add-modules javafx.controls"

javac ${COMP_OPT} ${MOD_PATH} ${MOD_OPT} -d ${CLASS_PATH} ${SOURCE_PATH}

if ! [[ -z $1 ]] && { [[ "$1" != 'v' ]] || [[ "$1" = ' ' ]]; };then
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
