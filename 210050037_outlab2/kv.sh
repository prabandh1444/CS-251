
file='store.txt'
Add(){
    echo "$1 $(date) $2" >> store.txt
}
displayInfo(){
    i=1  
echo "Name OrderID"
while read line; 
do  

#Reading each line  
echo "Order No. $i : $line"  
i=$((i+1))  
done < $file 
}
getOrderID(){
echo "Order IDs found are"
while read line; do
    for word in $line; do
        if [[ $word == $1 ]]; then
          line1=($line)
          echo "${line1[8]}"
        fi
    done
done <$file
}

"$@"

