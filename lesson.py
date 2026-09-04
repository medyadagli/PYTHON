print("Mini shopping system")
bakiye=float(input("Kullanıcıdan bakiye al:"))
urun_fiyatı=float(input("Kullanıcıdan ürün fiyatı al:"))
if urun_fiyatı <= bakiye:
    print("Purchase successful!")
    bakiye -= urun_fiyatı
else:
    print("Not enough money!")

print(bakiye)