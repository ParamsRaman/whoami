#!/bin/bash

# Assemble the dataset

rm ../data/csv/biglist.csv
#cat ../data/csv/datapacks/australia.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/bangladesh.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/brazil.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/canada.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/china.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
3cat ../data/csv/datapacks/colombia.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/france.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/germany.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/greece.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/india-hindu.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/india-muslim.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/india-christian.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/india-northeast.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/iran.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/italy.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/japan.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/kenya.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/mexico.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/netherlands.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/philippines.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/poland.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/portugal.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/puerto-rico.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/russia.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/south-korea.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/spain.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/taiwan.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/turkey.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
#cat ../data/csv/datapacks/uk.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/us.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv
cat ../data/csv/datapacks/vietnam.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> ../data/csv/biglist.csv

NUM_LINES=8002
NUM_FEATURES=82

python gen_features.py ../data/csv/biglist.csv train.txt
wc -l train.txt
NUM_LINES=`wc -l train.txt |cut -f5 -d' '`
echo "total lines: $NUM_LINES"

python normalize_dataset.py train.txt ${NUM_LINES} ${NUM_FEATURES} > train_normalized.txt
#cat train.txt > train_normalized.txt

python compact_classes.py train_normalized.txt > train_compacted.txt

wc -l train_compacted.txt
x=`wc -l train_compacted.txt |cut -f5 -d' '`
a=0.75
b=0.25
#tr_p=$(round $x/$a 2)
#te_p=$(round $x/$b 2)
tr_p=5500
te_p=1300

echo "total lines: $x, tr %: ${tr_p}, te %: ${te_p}"

cat train_compacted.txt | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' >> toto
mv toto train_compacted.txt

head -n ${tr_p} train_compacted.txt > train2.txt
tail -n ${te_p} train_compacted.txt > test2.txt

#rm train_normalized.txt train_compacted.txt

scp -v train2.txt test2.txt ramanp@rossmann-fe01.rcac.purdue.edu:/group/ml/data/mlr/names/


# Generate prediction
#python predict.py pmlr.model9 compact_mapping.txt "Michael Jordan"

## Backup commands ##
#awk 'BEGIN{FS="\t"; OFS=","} {$2=$1;$1="";$3='72';print}' fr_boys.txt
#sed 's/  */:/g' russian_boys.txt
#sed 's/  */:/g' tmp.tmp |cut -f3 -d':'
#cut -f1,2 -d',' names.csv |tr ',' '\n'|sed '/^$/d' > longlist.txt

#cat ../data/csv/names.csv | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' > ../data/csv/random.csv

