#!/usr/bin/env python
# coding: utf-8

# # Veri Tipi Değiştirme   

# In[ ]:


a = "5"
b= 10
print("Sayi toplam : ",int(a)+b)
print("String Toplam  : ",a+str(b))


# # LİSTE KOMUTLARI  

# In[ ]:


liste=[1,5,2,3,4]
print("Uzunluk : ",len(liste))
print("Üçüncü eleman  : ",liste[2])
print("Son eleman : ",liste[-1])
print("0 dan 2 ye : ",liste[0:3])
liste.append(9)
print("9 eklendi : ",liste)
liste.remove(2)
print("2 silindi : ",liste)
liste.sort()
print("Sirali liste : ",liste)
liste.insert(2,11)
print("2. indexe 11 eklendi : ",liste)
print("kaç 13 var ",liste.count(13))
print("5 kaçıncı indexte ",liste.index(5))


# # DİCTİONARY BASİCS 

# In[ ]:


ing_sozluk = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
print(ing_sozluk.keys())
print(ing_sozluk.values())
ing_sozluk["yellow"]="sarı"
print(ing_sozluk)


# In[ ]:


ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))


# # TUPLE  

# In[ ]:


t = (1,2,3,3,4,5,6)
a = 1,2,3,4,5,6
print("a nin tipi : ",type(a))
t.count(3)


# # Hesap Makinesi 

# In[ ]:


a=int(input("1. sayiyi giriniz :  "))
b=int(input("2. sayiyi giriniz  :  "))

print("İslem Seçiniz")
print("1 = Toplama")
print("2 = Çıkarma")
print("3 = Çarpma")
print("4 = Bölme")

islem=int(input("İslem Seçiniz : "))

if islem ==1:
    sonuc=a+b
    print("{} ve {}  nın toplamı = ".format(a,b),sonuc)
elif islem ==2:
    sonuc=a-b
    print("{} ve {}  nın farkı = ".format(a,b),sonuc)
elif islem ==3:
    sonuc=a*b
    print("{} ve {}  nın çarpımı = ".format(a,b),sonuc)
elif islem ==4:
    sonuc=a/b
    print("{} ve {}  nın bölümü = ".format(a,b),sonuc)
else:
    print("Geçerli işlem giriniz !!! ")


# # Faktoriyel  

# In[ ]:


x=int(input("Sayi giriniz : "))

faktoriyel=1

for i in range(faktoriyel,x+1):
    faktoriyel=faktoriyel*i
print("Faktoriyel : ",faktoriyel)


# # Maxi Bulma 

# In[ ]:


liste2=[1,5,9,2354,123456,213246,2222,200,985]

maxi=-10000000000
for each in liste2:
    if(each>maxi):
        maxi=each
    else:
        continue
print(maxi)


# # TOPLAM 

# In[ ]:


a=int(input("Sayi giriniz : "))
b=int(input("Sayi giriniz : "))
c=int(input("Sayi giriniz : "))

liste=[a,b,c]

toplam=0

for each in liste:
    toplam=toplam+each
    
print(toplam)


# # YÜZYIL HESAPLAMA

# In[ ]:


yil=int(input("Yil giriniz : "))

str_yil=str(yil)

if (len(str_yil)<3):
    yy=1
    print("Yüzyıl",yy)
elif (len(str_yil)==3):
    yy=int(str_yil[0])+1
    print("Yüzyıl : ",yy)
elif (len(str_yil)==4):
    yy=int(str_yil[0:2])+1
    print("Yüzyıl",yy)
else:
    print("Geçeri değer giriniz ")


# # WHİLE  

# In[ ]:


i=0 
while i !=5:
    print("i nin degeri : ",i)
    i+=1
print(i ," 5 e eşittir")


# # TEK ÇİFT

# In[ ]:


a=0
while a<11:
    a+=1
    islem=list(divmod(a,2))[1]
    if islem==0:
        print("{} Çift Sayidir".format(a))
    elif islem==1:
        print("{} Tek Sayidir".format(a))
    continue


# # FONKSİYONLAR 

# In[ ]:


def atoplambkare(a,b):
    atoplambkare= a**2 + 2*a*b + b**2
    return atoplambkare


# # BOOLE FONKSİYONLARI

# In[ ]:


t = True
f = False
print(type(t)) 
print(t and f) 
print(t or f)  
print(not t)   
print(t != f)

