#!/bin/bash
exchange_name=$1

waitforjobs() {
    while test $(jobs -p | wc -w) -ge "$1"; do wait -n; done
}


echo exchange,pair,token0,token1,block,numtransactions,mev

for file in `find ../mev/data-scripts/$exchange_name-processed/ -type f -exec wc -l {} + | sort -rn | tr -s ' ' | cut -d' ' -f3 | grep 0x | head -n 10`
do
    temp=${file%.csv}
    address=${temp##*/}
    for block in `sort -rt, -k2 -n ../mev/data-scripts/active-region/$exchange_name/txcount_$address.csv | grep ,[0-9]$ | head -n 30 | cut -f1 -d,`
    do
        cmd="python3 aggregate_data.py -b $block -a $address -e $exchange_name -c &"
        waitforjobs 20
        eval $cmd

    done
    #wait
done

