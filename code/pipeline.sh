#!/bin/bash

# the round function:
#round()
#{
#    echo $(printf %.$2f $(echo "scale=$2;(((10^$2)*$1)+0.5)*(10^$2)" | bc))
#};

python gen_features.py ../data/csv/names.csv train.txt
wc -l train.txt
x=`wc -l train.txt |cut -f5 -d' '`
x=1133
echo "total lines: $x"

NUM_FEATURES=62
python normalize_dataset.py train.txt 1133 ${NUM_FEATURES} > train_normalized.txt

python compact_classes.py train_normalized.txt > train_compacted.txt
wc -l train_compacted.txt
x=`wc -l train_compacted.txt |cut -f5 -d' '`
a=0.75
b=0.25
#tr_p=$(round $x/$a 2)
#te_p=$(round $x/$b 2)
tr_p=800
te_p=200

echo "total lines: $x, tr %: ${tr_p}, te %: ${te_p}"

head -n ${tr_p} train_compacted.txt > train2.txt
tail -n ${te_p} train_compacted.txt > test2.txt

rm train_normalized.txt train_compacted.txt

#scp -v train2.txt test2.txt ramanp@rossmann-fe01.rcac.purdue.edu:/group/ml/data/mlr/names/

## Backup commands ##
#awk 'BEGIN{FS="\t"; OFS=","} {$2=$1;$1="";$3='72';print}' fr_boys.txt
#sed 's/  */:/g' russian_boys.txt
#sed 's/  */:/g' tmp.tmp |cut -f3 -d':'


