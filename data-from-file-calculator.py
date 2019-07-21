#example
eklenecek_liste = []
def not_hesapla(son_not):
    if son_not >= 90 and  son_not <=100:
        harf = "AA"
    elif son_not >= 80 and  son_not <90:
        harf = "BA"
    elif son_not >= 70 and  son_not <80:
        harf = "BB"
    elif son_not >= 60 and  son_not <70:
        harf = "CB"
    elif son_not >= 50 and  son_not <=60:
        harf = "CC"
    elif son_not <50 and son_not >=0:
        harf = "FD"
    else:
        print("Geçersiz bir not değeri algılandı...")
    return "İsim : " + isim + "\n" + "Puan ortalaması : " + str(son_not) + "\nPuan Harf Değeri : " + harf + "\n\n"

with open("dosya.txt","r",encoding="utf-8") as file:
    for i in file:
        liste = i.split(",")
        isim = liste[0]
        not1 = int(liste[1])
        not2 = int(liste[2])
        not3 = int(liste[3])
        not_ort = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)
        eklenecek_liste.append(not_hesapla(not_ort))

with open("Hesaplanmis.txt","w",encoding="utf-8") as file2:
    for x in eklenecek_liste:
        file2.write(x)