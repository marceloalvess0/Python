import time

def cronometro():
    contador_s=0
    contador_m=0
    contador_h=0
    while True:
        time.sleep(1)
        contador_s=(contador_s+1)
        if (contador_s==(60)):
            contador_s=0
            contador_m=contador_m+1
        if (contador_m==60):
            contador_m=0
            contador_h==contador_h+1
        print("{}s:{}m:{}h".format(contador_s,contador_m,contador_h))
if __name__=="__main__":
    cronometro()