import os
import platform

print(platform.system())  #列出這台電腦的作業系統

d = []
os.system('start testrpc --gaslimit 5000000')  #執行cmd指令

#linux的是 gnome-terminal -e "bash -c '要打的指令; exec bash'"
# a = " gnome-terminal -e \"bash -c \'要打的指令; exec bash\'\" "
#os.system(a)


a = os.popen('tasklist').readlines()  #執行cmd指令（但取值）
for i in a:
    if 'cmd.exe' in i:
        d.append(i)
        print(i)

print('------------------------------------------')
print(d[-2][30:34])   #pid的部份（30-34），而-2那個是本次的為倒數第二個cmd（以後要依情況）

k = "taskkill /pid "
k = k + d[-2][30:34]

print(k)

os.system(k)  #執行關閉process的程式碼（taskkill /pid 程序pid）
