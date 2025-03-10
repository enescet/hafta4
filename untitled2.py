g = "Dünya Dopingle Mücadele Ajansı (WADA) çok sayıda Türk sporcuda doping tespit edildiğini açıkladı. Yapılan açıklamaya göre; halterde 7, boksta 3 ve güreşte 2 sporcu doping cezası aldı."
kelimeler = g.split(' ')

def donustur(a):
    sayac = []
    for kelime in a:
        uzunluk = len(kelime)
        sayac.append(uzunluk)
        print(uzunluk)
    return sayac

b = donustur(kelimeler)
print(b)
