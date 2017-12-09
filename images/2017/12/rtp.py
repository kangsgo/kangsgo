#-*-coding:utf-8-*-
#作者:kangsgo
#config.txt 设置本身不存在的虚拟原子(要剔除的)
#使用:python rtp.py file name
#例如:python rtp.py SEP_GMX.top SEP

import sys

filename=sys.argv[1]
name=sys.argv[2]
ffbond=open(filename,'r')
ffbondline=ffbond.readlines()

ban=[]
for j in open('config.txt','r'):
    j=j.rstrip('\n')
    ban.append(j)
    
print('''[ bondedtypes ]
; bonds  angles  dihedrals  impropers all_dihedrals nrexcl HH14 RemoveDih
     1       1          9          4        1         3      1     0''')

print('[ '+name+' ]')

print(' [ atoms ]')
data=False
for i in ffbondline:
    if data:
        if i.startswith(';'):
            pass
        elif i=='\n':
            data=False
        else:
            new=i.split()
            if new[4] in ban: 
                pass
            else:
                print(new[4].rjust(7)+new[1].rjust(6)+new[6].rjust(18)+new[5].rjust(6))
    if i=='[ atoms ]\n':
        data=True


print(' [ bonds ]')
data=False
for i in ffbondline:
    if data:
        if i.startswith(';'):
            pass
        elif i=='\n':
            data=False
        else:
            new=i.split()
            if new[6] in ban or new[8] in ban: 
                pass
            else:
                print(new[6].rjust(7)+new[8].rjust(6)+new[3].rjust(18)+new[4].rjust(15))
    if i=='[ bonds ]\n':
        data=True


print(' [ angles ]')
data=False
for i in ffbondline:
    if data:
        if i.startswith(';'):
            pass
        elif i=='\n':
            data=False
        else:
            new=i.split()
            if new[7] in ban or new[9] in ban or new[11] in ban: 
                pass
            else:
                print(new[7].rjust(7)+new[9].rjust(6)+new[11].rjust(6)+new[4].rjust(16)+'  '+new[5].rjust(16))
    if i=='[ angles ]\n':
        data=True


print(' [ dihedrals ] ; propers')
data=False
for i in ffbondline:
    if data:
        if i.startswith(';'):
            pass
        elif i=='\n':
            data=False
        else:
            new=i.split()
            if new[9][:-1] in ban or new[10][:-1] in ban or new[11][:-1] in ban or new[12] in ban: 
                pass
            else:
                print(new[9][:-1].rjust(6)+new[10][:-1].rjust(6)+new[11][:-1].rjust(6)+new[12].rjust(10)+new[5].rjust(10)+new[6].rjust(10)+new[4].rjust(6))
    if i=='[ dihedrals ] ; propers\n':
        data=True


print(' [ impropers ]')
data=False
for i in ffbondline:
    if data:
        if i.startswith(';'):
            pass
        elif i=='\n':
            data=False
        else:
            new=i.split()
            if new[9][:-1] in ban or new[10][:-1] in ban or new[11][:-1] in ban or new[12] in ban: 
                pass
            else:
                print(new[9][:-1].rjust(6)+new[10][:-1].rjust(6)+new[11][:-1].rjust(6)+new[12].rjust(6)+new[5].rjust(10)+new[6].rjust(12)+new[4].rjust(6))
    if i=='[ dihedrals ] ; impropers\n':
        data=True