touch cypher.txt
sed -e 's/-/ /g' <$1>cypher.txt
x=$3
awk '{if(NR == FNR && NR <= x+1){ key[$1]=$2; next }
      else if(NR != FNR){for(i=1;i<=NF;i++){c++; if(c <= x)printf("%s ",key[$i])}}}' x=$x  cypher.txt $2
awk '{for(i=1;i<=NF;i++){c++; if(c>x)printf("%s ",$i)}}' x=$x $2
echo ""
 rm cypher.txt


