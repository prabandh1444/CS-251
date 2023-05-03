#!/bin/bash
touch in.txt
touch out1.txt
touch out2.txt
sed -e 's/a/10/g;s/b/11/g;s/c/12/g;s/d/13/g;s/e/14/g;s/f/15/g' <$1>in.txt
awk '{
     if(NR == 1){t_cases = $1;}
     else if(NR%3 == 2){in_base=$1; out_base=$2;}
     else if(NR%3 == 0){sum=0;for(i=1;i<=NF;i++) {sum=sum+($i)*(in_base)^(NF-i);}}
     else if(NR%3 == 1){sum1=0;for(i=1;i<=NF;i++) {sum1=sum1+($i)*(in_base)^(NF-i);}
                      t_sum=sum1+sum;
                      while(t_sum>0){
                               printf("%d ",t_sum%out_base) > "out1.txt"
                               t_sum = int(t_sum/out_base);
                        }
                        print "" > "out1.txt"
                        }
                        }' in.txt
awk '{for(i=NF;i>=1;i--){printf("%d ",$i) > "out2.txt"} print "" > "out2.txt"}' out1.txt
sed -e 's/10/a/g;s/11/b/g;s/12/c/g;s/13/d/g;s/14/e/g;s/15/f/g' <out2.txt >$2
rm in.txt
rm out1.txt
rm out2.txt
