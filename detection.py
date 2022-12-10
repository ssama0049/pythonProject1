import subprocess
def ip():
    s = open("2.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    h = str(input("Введите ip от которого вы будете защищаться:"))
    if (h in u):
        subprocess.call(
            f'netsh advfirewall firewall add rule name="Блокировка IP" dir=out interface=any action=block remoteip={h}',
            shell=True)
    else:
        print("???")