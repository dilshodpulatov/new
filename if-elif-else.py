# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:05:38 2021

@author: uzbdap
"""

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")
    
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")
    
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4 or yosh>=60:
    print('Sizga kirish bepul.')
elif yosh<=18:
    print('Sizga kirish 10000 so\'m')
else:
    print('Sizga kirish 20000 so\'m')
    
# son1 = float(input('1-Sonni kiriting '))
# son2 = float(input('2-Sonni kiriting '))
# if son1==son2:
#     print(f'{son1} = {son2}')
# elif son1 < son2:
#     print(f'{son1} < {son2}')
# else:
#     print(f'{son1} > {son2}')

mahsulotlar = ['anor','non','go\'sht','olma','tarvuz', 'behi', 'hurmo', ]
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni qushing: "))
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f" Do'konimizda {mahsulot} bor")
    else:
        print(f" Do'konimizda {mahsulot} yo'q")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar:                    # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
#Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q 
#mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
#"Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar 
#do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")    