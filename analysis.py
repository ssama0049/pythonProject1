def csv():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    print(u)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        with open(f"{h}.json","r") as f:
            print(f.read())