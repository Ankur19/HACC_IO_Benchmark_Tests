#!/bin/bash

#export PATH=/app/mpiccInstall/bin:$PATH

#cd /app/stream/FTP/Code/Versions

echo "Which version?"
echo "[ 1: Local, 2: Volumes, 3: BindMounts ]"
read version

if [ $version -eq 1 ]
then
	resultPath=$PWD/localResults
	mkdir localResults
else
	export PATH=/app/mpiccInstall/bin:$PATH
	
	if [ $version -eq 2 ]
	then
		resultPath=$PWD/volumeResults
		mkdir volumeResults
	else
		resultPath=$PWD/bindMountResults
		mkdir bindMountResults
	fi
fi

make CXX=mpicc LDLIBS="-lstdc++"

arr=( 10 25 50 100 250 500 1000 )

rank=( 1 2 3 4 )

for i in "${arr[@]}"
do
	x=$((100000*i))
	
	#mpicc -O -DSTREAM_ARRAY_SIZE="$x" stream_mpi.c -o stream."$i"M
	
	for j in "${rank[@]}"
	do
		mpirun -n "$j" ./hacc_io "$x" results/mpitest >> "$resultPath"/result.txt
	done
	
	cd results
	rm *
	cd ..
done
