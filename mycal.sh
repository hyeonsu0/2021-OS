#!bin/bash
# 2021-03-29 soo

oper=$1
num1=$(<$2num1.txt)
num2=$(<$2num2.txt)

if [ -z "$1" ]; then
  echo "none operator parameter"
  echo -e "choice operator \n1)add\n2)sub\n3)div\n4)mul\n"
  read -p "your choice: " oper
fi

case $oper in
  1|add)
    temp=`expr $num1 + $num2`
    op="add"
;;
  2|sub)
    temp=`expr $num1 - $num2`
    op="sub"
;;
  3|div)
    temp=`expr $num1 / $num2`
    op="div"
;;
  4|mul)
    temp=`expr $num1 \* $num2`
    op="mul"
;;
esac

echo -e "num1 : $num1\nnum2 : $num2\nop : $op\ntotal : $temp"
