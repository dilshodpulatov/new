# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 09:52:35 2021

@author: uzbdap
"""

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")
# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)
# kinolar = [] # bo'sh ro'yxat
# print("5 ta eng sevimli kinolaringizni kiriting?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     kinolar.append(input(f"{n+1}-kinoni nomini kiriting: "))
# print(kinolar)
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)