import os
d = []
os.system('start testrpc --gaslimit 5000000')  #執行cmd指令


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
