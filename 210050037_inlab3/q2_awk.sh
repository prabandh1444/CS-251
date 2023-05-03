f(){
file=$1
sed -i 's/ //g' file
file=$(echo $file | tr a-z A-Z)
awk '{for(i=1; i <= NF; i++){sum=sum+($i*pow((8+2*$0),i-1))} END print sum}'file;
}
f $1
