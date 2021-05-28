#!/usr/bin/python
#20210429 SH.Kang package
import my_pkg

if __name__ == '__main__':
        while(True):
                menu = input("Select menu: 1) average 2) fibonacci 3) exit ?")
                if(menu=='1'):
                       my_pkg.aver()
                elif(menu=='2'):
                       my_pkg.fibo()
                elif(menu=='3'):
                        print("eixt the program...")
                        break
