#!/bin/bash                                                                                                  

SESSIONNAME="eurobot"
tmux has-session -t $SESSIONNAME &> /dev/null

if [ $? != 0 ] 
 then
    tmux new-session -s $SESSIONNAME -n script -d
    tmux send-keys -t $SESSIONNAME "~/Projects/eurobot/setup/launch.sh" C-m 
fi

