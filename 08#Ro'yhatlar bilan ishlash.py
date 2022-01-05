# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
state = [ "Uzbekistan", "Russia", "China", "USA", "Japan", "France"]
print(state)
#Ro'yxatning uzunligini konsolga chiqaring
#print(len(state))
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(state))
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print(sorted(state, reverse = True))
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# state.reverse()
# print(state)
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# state.sort()
# print(state)
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120,1200,2))
#print(juft_sonlar)
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
jami = sum(juft_sonlar)
print( "Jami: ",  jami)
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
ayirma = juft_sonlar[-1]-juft_sonlar[0]
print(ayirma)
#Ro'yxatdagi elementlar sonini hisoblang
print( "Elementlar soni:", len(juft_sonlar))
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[:7], juft_sonlar[234:240], juft_sonlar[533:])