#  meno = input("zadajte meno: ")
# vek = input("zadajte vek: ")
# print("Zdravim " + meno)
# print("Vas vek " + vek)

prvy = float(input("zadaj km pre prvý deň: "))
treba_km = float(input("zadaj cieľové km: "))
den = 0
while prvy < treba_km:
        prvy = prvy*1,1
        den += 1
print("na " + den + ". den prebehne " + prvy + " km")