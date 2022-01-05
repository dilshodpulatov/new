# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 09:56:25 2021

@author: uzbdap
"""
# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

# cars = ['audi','bmw','volvo','kia','hyundai', 'gm']
# for avto in cars: # cars ichidadi har bir avto uchun ...
#     if avto == 'gm':  # ... agar avto gm ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.

# cars = ['audi','bmw','volvo','kia','hyundai', 'gm']
# for avto in cars: # cars ichidadi har bir avto uchun ...
#     if avto != 'gm':  # ... agar avto gm ga teng bo'lsa ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, 
# Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  
# matnini konsolga chiqaring.

# ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")
    
# login = input("login ismingiz?\n>>>")
# if login.lower() == 'admin':
#         print(f"Xush kelibsiz, {login.title()} Foydalanuvchilar ro'yhatini ko'rasizmi?")
# else: 
#         print(f"Xush kelibsiz {login.title()}")

# son = float(input("Son kiriting>>>"))
# son2 = float(input('2-sonni kiriting>>>'))
# if son == son2:
#     print(f'Sonlar teng: {son}={son2}')
# else: print('sonlar teng emas') 

# son = float(input("Son kiriting>>>"))
# if son>0:
#     print('Musbat son')
# else: print('Manfiy son')

son = float(input("Son kiriting>>>"))
if son>0: print(son**(1/2))
else: print('Musbat son kiriting')