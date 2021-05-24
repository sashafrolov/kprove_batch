#!/bin/bash
exchange_name=$1
directory=$2

waitforjobs() {
    while test $(jobs -p | wc -w) -ge "$1"; do wait -n; done
}


echo exchange,pair,token0,token1,block,numtransactions,mev

for file in `find ../mev/data-scripts/latest-data/$exchange_name-processed/ -type f -exec wc -l {} + | sort -rn | tr -s ' ' | cut -d' ' -f3 | grep 0x | head -n 15`
do
    temp=${file%.csv}
    address=${temp##*/}
    for block in `sort -rt, -k2 -n ../mev/data-scripts/latest-data/active-region/$exchange_name/txcount_$address.csv | awk -F, '$2 < 12' | head -n 40 | cut -f1 -d,`
    do
        cmd="python3 aggregate_data.py -b $block -a $address -e $exchange_name -c -d $directory"
        waitforjobs 5
        eval $cmd
    done
    #wait
done

