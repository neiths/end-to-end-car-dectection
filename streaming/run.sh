#!/bin/bash

cmd=$1

usage() {
    echo "run.sh <command> <arguments>"
    echo "Available commands:"
    echo "  register_connector |    register a new kafka connector"
    echo "  start_streamning |  start streaming to kafka"
    echo "Available arguments:"
    echo " [connector config path] path to connector config, for command register_connector only"
}

if [[ -z "$cmd" ]]; then
    echo "Missing conmmand"
    usage
    exit 1
fi

case $cmd in 
    register_connector)
        if [[ -z "$2" ]]; then
            echo "Missing connector config path"
            usage
            exit 1
        else
            echo "Registering a new connector from $2"

            curl -s -X POST -H 'Content-Type: application/json' --data @$2 http://localhost:8083/connectors

        fi
        ;;

    generate_schemas)
        python generate_schemas.py --min_features 2 --max_features 10 --num_schemas 1
        ;;

    *)
        echo "Unknown command: $cmd"
        usage 
        exit 1
        ;;
esac
