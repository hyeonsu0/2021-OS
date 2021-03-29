#!bin/bash
# 2021-03-29 soo

local oper = $1
num1=$(<num1.txt)
num2=$(<num2.txt)

if [ -z "$oper" ]; then
  echo "choice operator 1)add 2)sub 3)div 4)mul"
  read -p "Enter your choice: " oper
fi

case $oper in
  1|add)
    temp = `expr$num1 + $num2`
    echo "$num1 + $num2 = $temp"
  2|sub)
    temp = `expr$num1 - $num2`
    echo "$num1 - $num2 = $temp"
  3|div)
    temp = `expr$num1 / $num2`
    echo "$num1 / $num2 = $temp"
  4|mul)
    temp = `expr$num1 * $num2`
    echo "$num1 * $num2 = $temp"
