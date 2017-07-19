#!bin/bash
cd customizedMesos-master/build
./bin/mesos-agent.sh --master=127.0.0.1:5050 --work_dir=/var/lib/mesos
