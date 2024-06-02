#!/bin/bash

pull_repos() {
    for dir in "$1"/*; do
        if [ -d "$dir" ]; then
            if [ -d "$dir/.git" ]; then
                echo "Exec git pull inside $dir"
                (cd "$dir" && git pull)
            else
                pull_repos "$dir"
            fi
        fi
    done
}

MAIN_DIR="."

pull_repos "$MAIN_DIR"
