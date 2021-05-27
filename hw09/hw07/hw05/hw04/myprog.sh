#!/bin/bash
# 2021-03-29 soo

mkdir -p temp
echo "create temp directory"
mv *.txt temp
mv mycal.sh temp
echo "move filed to temp directory"

echo -e "choice operator\n1)add\n2)sub\n3)div\n4)mul\n" 
read -p "your choice: " oper

case $oper in
	1|add)
		echo "your choice is add"
		bash temp/mycal.sh 1 temp/;;
	2|sub)
		echo "your choice is sub"
		bash temp/mycal.sh 2 temp/;;
	3|div)
		echo "your choice is div"
		bash temp/mycal.sh 3 temp/;;
	4|mul)
		echo "your choice is mul"
		bash temp/mycal.sh 4 temp/;;
	*)
		echo "invalid choice"
		bash temp/mycal.sh;;
esac
