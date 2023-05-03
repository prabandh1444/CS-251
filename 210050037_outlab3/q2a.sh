#!/bin/bash
touch dummy.txt
touch out.txt
touch out1.txt
sed -e 's/:/ /g;s/_/ /g;s@/@ @g;s/,/ /g' <$1>dummy.txt
awk '{if(NR == 1){printf("FirstName ") > "out.txt"
                  printf("LastName ") > "out.txt"
                  printf("Date ") > "out.txt"
                  printf("Time ") > "out.txt"
                  print "" > "out.txt"}
      else{printf("%s ",$1) > "out.txt"
      printf("%s ",$2) > "out.txt"
      printf("%s/",$5) > "out.txt"
      if($4 == "01") printf("January/") > "out.txt"
      if($4 == "02") printf("Feberuary/") > "out.txt"
      if($4 == "03") printf("March/") > "out.txt"
      if($4 == "04") printf("April/") > "out.txt"
      if($4 == "05") printf("May/") > "out.txt"
      if($4 == "06") printf("June/") > "out.txt"
      if($4 == "07") printf("July/") > "out.txt"
      if($4 == "08") printf("August/") > "out.txt"
      if($4 == "09") printf("September/") > "out.txt"
      if($4 == "10") printf("October/") > "out.txt"
      if($4 == "11") printf("November/") > "out.txt"
      if($4 == "12") printf("December/") > "out.txt"
      printf("%s ",$3) > "out.txt"
      if(int($6) > 12) printf("%d:%sPM",int($6)-12,$7) > "out.txt"
      if(int($6) == 12) printf("%d:%sPM",12,$7) > "out.txt"
      if(int($6) < 12) printf("%d:%sAM",int($6),$7) > "out.txt"
      print "" > "out.txt"}}
      ' dummy.txt
sed -e 's/ /,/g;s@/@ @g'<out.txt>out1.txt
while IFS= read -r line
do
echo $line >> "$2"
done<"out1.txt"
cat dummy.txt
cat out1.txt
rm out1.txt
rm dummy.txt
