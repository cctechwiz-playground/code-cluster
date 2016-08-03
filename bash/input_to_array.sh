##Version one - mine
####################
#readarray countries;
#declare -a mod_countries;

#for c in "${countries[@]}"; do
#    mod_countries[${#mod_countries[*]}]=`echo -n "."; echo -n $c | cut -c 2-;`;
#done;

#echo ${mod_countries[@]}


##Version two - Weird spacing
#############################
#sed 's/^[A-Z]/./'|paste -s


##Version three - I like this best
##################################
arr=();
while read i; do
	arr=("${arr[@]}" "$i");
done;	

arr=( ${arr[@]/[A-Z]/.} );
echo ${arr[@]};


##Version four - awk version (I like it but it's not using arrays)
##################################################################
#awk 'BEGIN{ORS=" ";} {gsub(/^./,".",$1); print}'


arr=();
while read i; do
    arr=("${arr[@]}" "$i");
done;

arr=( ${arr[@]/*[aA]*/} );
echo ${arr[@]};

##Reverse a string
awk '{ for(i=length;i!=0;i--)x=x substr($0,i,1);}END{print x}'