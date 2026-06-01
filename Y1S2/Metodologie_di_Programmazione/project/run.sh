#!/bin/bash

#set -xe

if ! [ -z $1 ];then
    COMP_OPT="-Werror -g:none -Xlint"
    if [ "$1" = 'debug' ];then
        COMP_OPT="-Werror -g:lines -g:vars -g:source -verbose -Xlint"
    fi
fi

RUN_OPT=""

SOURCE_PATH="src/*.java"
CLASS_PATH="cls"

MOD_PATH="--module-path ${JAVA_FX_PATH}" 
MOD_OPT="--add-modules javafx.controls"

javac ${COMP_OPT} ${MOD_PATH} ${MOD_OPT} -d ${CLASS_PATH} ${SOURCE_PATH}

if ! [[ -z $1 ]] && { [[ "$1" != 'debug' ]] || [[ "$1" = ' ' ]]; };then
    if [ "$1" = 'r' ]; then
            if ! [ -z $2 ] ; then
                if [ "$2" = 'O' ];then
                    RUN_OPT="-XX:+UseParallelGC" #-XX:+UseLargePages" does not work, maybe i can make it work
                fi
                if [ "$2" = 'debug' ]; then
                    RUN_OPT="-verbose:class -verbose:gc -verbose:modules -Xlog:all=warning:stdout:uptime,level,tags"
                fi
                if ! [ -z $3 ];then
                    java ${RUN_OPT} ${MOD_PATH} ${MOD_OPT} --enable-native-access=javafx.graphics -cp "${CLASS_PATH}" $3
                    else
                        java ${RUN_OPT} ${MOD_PATH} ${MOD_OPT} --enable-native-access=javafx.graphics -cp "${CLASS_PATH}" $2
                fi
                else
            echo "Insert name of the class you want to run"  
            fi
        else
            echo "Use argument flag 'r'"
    fi

fi
