#!/bin/bash
if [[ $2 == "-lines" ]]
then 
    awk '{} END {print NR " lines"}' $1
elif [[ $2 == "-paras" ]]
then 
    awk '{if(NF == 0){counter++}} END {print counter+1 " paragraphs"}' $1
elif [[ $2 == "-words" ]]
then 
     awk '{for(i=1;i<=NF;i++)c++}END{print c " words"}' $1
elif [[ $2 == "-characters" ]]
then echo $(awk 'BEGIN{FS=""}{for(i=1;i<=NF;i++){if($i != " ")c++}}END{print c}' $1) "characters" 
else 
	echo $(awk 'BEGIN{FS=""}{for(i=1;i<=NF;i++i){if($i != " ")c++}}END{print c}' $1 ) "characters," $(awk '{for(i=1;i<=NF;i++)c++}END{print c " words"}' $1)"," $( awk '{} END {print NR " lines"}' $1)","$(awk  '{if(NF == 0){counter++}} END {print counter+1 " paragraphs"}' $1)
fi
