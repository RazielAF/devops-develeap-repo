#!/bin/bash
sleep 10
declare -a endpoints=("beans" "caches" "conditions" "env" "info" "loggers" "metrics" "scheduledtasks" "mappings" "health")
for endpoint in ${endpoints[@]}
do
    response=$(curl -i http://${1}:${2}/actuator/${endpoint} 2>/dev/null | head -n 1 | cut -d$' ' -f2)
    if [ $response -eq 200 ]
    then 
        echo "test ${endpoint} passed - ${response}"
    else
        echo "test ${endpoint} fail - ${response}"
    fi
done
  