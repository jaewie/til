# Killing all child processes

`pkill -TERM -P 1234` where 1234 is the parent process or `CPIDS=$(pgrep -P 1234); (sleep 33 && kill -KILL $CPIDS &); kill -TERM $CPIDS`
