#!/bin/bash
for i in `seq 1 2`;
    do
        echo $i
        python emit_logs_topic.py
    done    