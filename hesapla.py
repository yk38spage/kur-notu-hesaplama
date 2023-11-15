import os
from urllib.request import urlopen

def kurhesap():
    print("\n1. aşama - Kur içi (In-class) notu hesaplama:")
    quiz1 = float(input("1. quiz notunuzu (QUIZ 1 - CB) giriniz: "))
    quiz2 = float(input("2. quiz notunuzu (QUIZ 2 - Listening) giriniz: "))
    quiz3 = float(input("3. quiz notunuzu (QUIZ 3 - Reading) giriniz: "))
    quiz4 = float(input("4. quiz notunuzu (QUIZ 4 - CB) giriniz: "))
    quiz5 = float(input("5. quiz notunuzu (QUIZ 5 - Outside R.) giriniz: "))

    quiz = (quiz1 + quiz2 + quiz3 + quiz4 + quiz5) / 5

    writing = float(input("Yazma (In-class Writing) notunuzu giriniz: "))
    perform = float(input("Performans (In-class Performance) notunuzu giriniz: "))
    project = float(input("Video proje (Video Project Assig.) notunuzu giriniz: "))
    online = float(input("Online Practice notunuzu giriniz: "))

    print("\n2. aşama - Kur bitirme (Level Exit Exam) sınav notları hesaplama:")
    exit_use = float(input("Use of English notunuzu giriniz: "))
    exit_writ = float(input("Yazma (Writing) notunuzu giriniz: "))
    exit_lis = float(input("Dinleme (Listening) notunuzu giriniz: "))
    exit_read = float(input("Okuma (Reading) notunuzu giriniz: "))
    exit_speak = float(input("Konuşma (Speaking) notunuzu giriniz: "))

    in_class = (quiz * 20 / 100) + (writing * 8 / 100) + (perform * 7 / 100) + (project * 5 / 100) + (online * 5 / 100)
    lvlexit = (exit_use * 15 / 100) + (exit_writ / 10) + (exit_lis / 10) + (exit_read / 10) + (exit_speak / 10)

    print(f"\nQuiz ortalamanız: {quiz}\nQuizlerden kazandığınız puan: {quiz * 20 / 100}\n")
    print(f"Kur içi (In-class) notunuz: {in_class * 100 / 45}\nKur içinden (In-class) kazandığınız puan: {in_class}\n")
    print(f"Kur bitirme (Level exit) notunuz: {lvlexit * 100 / 55}\nKur bitirmeden (Level exit) kazandığınız puan: {lvlexit}\n")

    mark = (in_class) + (lvlexit)
    print(f"Toplam puanınız: {mark}")

    if mark >= 70:
        print("Geçtiniz! Sonraki kurdan devam edeceksiniz. :)")
    else:
        print("Kaldınız. Kur tekrarı yapmanız gerek. :(")

    soralim()

def soralim():
    soru = str(input("\nTekrar yapmak ister misiniz? E/H: ").capitalize())

    if soru == "E":
        kurhesap()
    elif soru == "H":
        print("Görüşürüz!")
        bye_bye()
    else:
        print("Geçersiz seçenek.")
        soralim()

def sozlesmekabul():
    lisans = str(input("\nLisans sözleşmesini okudum, kabul ediyorum (K)/kabul etmiyorum(R). K/R: ").capitalize())
    if lisans == "K":
        with open("settings.json", "r+") as file:
            onayoku[0] = "license_agreement_acceptance = True\n"
            file.writelines(onayoku)
        print("Lisans sözleşmesini kabul ettiniz.")
        kurhesap()
    elif lisans == "R":
        with open("settings.json", "r+") as file:
            onayoku[0] = "license_agreement_acceptance = False\n"
            file.writelines(onayoku)
        print("Lisans sözleşmesini reddettiniz. Programdan çıkıyoruz.")
        bye_bye()
    else:
        print("Geçersiz seçenek.")
        sozlesmekabul()
    
def bye_bye():
    os.system("pause")
    exit()

print("""Kur Notu Hesaplama - ERÜ Hazırlık öğrencilerinin kur notlarını hesaplamasına yardımcı olur
Copyright (C) 2023  Yiğithan Karabel yk38

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.""")
print("\nKur notu hesaplamaya hoş geldiniz! (C) 2023 Yiğithan Karabel yk38\n")

if os.path.exists("settings.json") == False:
    olustur = open("settings.json", "w")
    olustur.write("""license_agreement_acceptance = 
                  
// This file is part of Kur Notu Hesaplama.
// 
// Kur Notu Hesaplama is free software: you can redistribute it and/or
// modify it under the terms of the GNU General Public License as 
// published by the Free Software Foundation, either version 3 of the 
// License, or (at your option) any later version.
// 
// Foobar is distributed in the hope that it will be useful, but WITHOUT 
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or 
// FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
// for more details.
// 
// You should have received a copy of the GNU General Public License along 
// with Kur Notu Hesaplama. If not, see <https://www.gnu.org/licenses/>.
""")
    olustur.close()

with open("settings.json", "r+") as file:
    onayoku = file.readlines()

if os.path.exists("LICENSE") == False:
    for kopyala in urlopen("https://www.gnu.org/licenses/gpl-3.0.txt"):
        lisansac = open("LICENSE", "ab+")
        lisansac.write(kopyala)
        lisansac.close()

lisansac = open("LICENSE", "r")

if onayoku[0] == "license_agreement_acceptance = True\n":
    kurhesap()
elif onayoku[0] == "license_agreement_acceptance = False\n":
    print(lisansac.read())
    print('Yukarıdaki lisans sözleşmesini reddettiğinizden ötürü programı kullanamazsınız. Program ile aynı dizinde bulunan "settings.json" dosyasını silip tekrar çalıştırmayı deneyin.')
    bye_bye()
else:
    print(lisansac.read())
    print("\nBu programı kullanmak için yukarıdaki lisans sözleşmesini onaylamanız gerekmektedir.")
    sozlesmekabul()

sozlesmekabul()