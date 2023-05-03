let a_before=0
 let a_after=1
 echo -n "$a_before "
 for((i=1;i<$1;i++))
do
        echo -n "$a_after " 
        let a=a_after
        let a_after=a_after+a_before
        let a_before=a
done
