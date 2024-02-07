# Koodi importib math mooduli, et kasutada matemaatilisi funktsioone.
import math

# Kalkulaator klass defineerib lihtsa kalkulaatori funktsioonid.
class Kalkulaator:
    # liida meetod liidab kaks arvu.
    def liida(self, num1, num2):
        return num1 + num2

    # lahuta meetod lahutab teise arvu esimesest.
    def lahuta(self, num1, num2):
        return num1 - num2

    # korruta meetod korrutab kaks arvu.
    def korruta(self, num1, num2):
        return num1 * num2

    # jaga meetod jagab esimese arvu teisega, kui teine arv pole null.
    def jaga(self, num1, num2):
        if num2 == 0:
            return "Viga! Ei saa nulliga jagada"
        else:
            return num1 / num2

# TäiendatudKalkulaator klass laiendab Kalkulaator klassi, lisades mõned täiendavad funktsioonid.
class TäiendatudKalkulaator(Kalkulaator):
    # protsent meetod arvutab protsendi kahe arvu vahel.
    def protsent(self, num1, num2):
        return (num1 * num2) / 100

    # ruutjuur meetod arvutab arvu ruutjuure.
    def ruutjuur(self, num1):
        return math.sqrt(num1)

    # astendamine meetod tõstab aluse astmesse.
    def astendamine(self, alus, aste):
        return alus ** aste

# Kalkulaatori_kasutusjuhised funktsioon annab kasutajale kalkulaatori kasutamise juhendid.
def Kalkulaatori_kasutusjuhised():
    print("\nKalkulaatori kasutusjuhised:")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("5. Protsent")
    print("6. Ruutjuur")
    print("7. Astendamine")
    print("0. Välju")

# Loodakse Kalkulaator objekt, mis on tegelikult TäiendatudKalkulaator objekt.
Kalkulaator = TäiendatudKalkulaator()

# While tsükkel jätkub kasutaja sisendi küsimise ja vastuste kuvamisega, kuni kasutaja sisestab "0" ehk väljub.
while True:
    Kalkulaatori_kasutusjuhised()
    valik = input("Sisesta valiku numer(0-7): ")

    if valik == "0":
        print("OFF")
        break

    # Kontrollitakse, millist tüüpi arvutust kasutaja soovib teha ja küsitakse vastavad arvud.
    if valik in("1", "2", "3", "4", "5"):
        num1 = float(input("Sisesta esimene arv: "))
        num2 = float(input("Sisesta teine arv: "))
    elif valik == "6":
        num1 = float(input("Sisesta arv: "))
    elif valik == "7":
        num1 = float(input("Sisesta alus: "))
        num2 = float(input("Sisesta aste: "))

    # Sõltuvalt kasutaja valikust kutsutakse vastav Kalkulaatori meetod ja kuvatakse tulemus.
    if valik == "1":
        print("Tulemus:", Kalkulaator.liida(num1, num2))
    elif valik == "2":
        print("Tulemus:", Kalkulaator.lahuta(num1, num2))
    elif valik == "3":
        print("Tulemus:", Kalkulaator.korruta(num1, num2))
    elif valik == "4":
        print("Tulemus:", Kalkulaator.jaga(num1, num2))
    elif valik == "5":
        print("Tulemus:", Kalkulaator.protsent(num1, num2))
    elif valik == "6":
        print("Tulemus:", Kalkulaator.ruutjuur(num1))
    elif valik == "7":
        print("Tulemus:", Kalkulaator.astendamine(num1, num2))
    else:
        print("Vigane sisend")