import  random
def getImei():
    r1 = 1000000 + random.randint(1,9000000)
    r2 = 1000000 + random.randint(1,9000000)
    input = str(r1) + str(r2)
    ch = list(input)
    a = 0
    b = 0
    for i in range(len(ch)):
        tt = int(ch[i])
        if (i % 2 == 0):
          a = a + tt
        else:
            temp = tt * 2
            b = b + temp / 10 + temp % 10

    last = int((a + b) % 10)
    if (last == 0):
        last = 0
    else:
       last = 10 - last
    return input + str(last)

imeiNu = int(input("请输入需要生成的imei数量:"))
with open("imei.txt","w",encoding="utf-8") as fw:
    for i in range(imeiNu):
        fw.write(getImei()+'\n')