import ipwhois
import json


import analysis
import detection

n = 1


while(n != 0):
    s = open("2.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    num1 = ["Поиск информации(нажмите 1)","Защита от атак(нажмите 2)"]
    for j in num1:
        print(j)
    k = str(input())
    if(k == "1"):
        num = str(input("Введите ip для работы:"))
        if (num in u):
            obj = ipwhois.IPWhois(num)
            res = obj.lookup_whois()
            r = json.dumps(res, indent=len(res))
            print(r)
            name = str(input("Введите имя JSON-файла:"))
            with open("1.txt", "a+") as f:
                f.write(f'{name}\n')
            with open(f"{name}.json", "a+") as f:
                f.write(r)
        else:
            print("NO")
        a = ["да", "нет"]
        r = "/".join(a)
        print(f"Хотите ли вы провести получить данные одного из уже имеющихся файлов?{r}")
        l = str(input("Введите ответ:"))
        if (l == a[0]):
            analysis.csv()

        elif (l == a[1]):
            print("ОК!")

        else:
            print("???")
    elif(k == "2"):
        detection.ip()
    else:
        print("???")
    ans = ["да", "нет"]
    ans_n = "/".join(ans)
    print(f"Хотите ли вы продолжить работу с данным ПО?{ans_n}")
    s = str(input("Введите ответ:"))
    if (s == ans[0]):
        n += 1
    elif (s == ans[1]):
        break
    else:
        print("Ничего непонятно")