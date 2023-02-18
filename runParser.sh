a=""
for i in {0..39}
do 
a+="ebay_data/items-$i.json "
done
python ebay_parser.py $a
sort -u users.dat > usersTest1.txt
