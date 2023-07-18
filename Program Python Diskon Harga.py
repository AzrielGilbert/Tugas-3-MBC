print("## Program Python Diskon Potongan Harga ##")
print("==========================================")
print("")

x = int(input("Total belanja: Rp. "))

if (x > 0):
    if x <= 100000:
        dis = x*0
        print("Maaf, anda tidak mendapat diskon")
    elif x <= 500000:
        dis = x*0.1
        print("Selamat, anda mendapat diskon: ", dis)
    elif x <= 1000000:
        dis = x*0.2
        print("Selamat, anda mendapat diskon: ",dis)
    elif 1000000 <= x:
        dis = x*0.3
        print("Selamat, anda mendapat diskon: ",dis)

    print("Total bayar: Rp. ", x-dis)
else:
        print("Unable to calculate")