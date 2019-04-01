tekst = "Anna, paweł, JulIA"

lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista)) #list

imie1 = lista[0]
print(imie1) #Anna

imieDuza = imie1.upper()
print(imieDuza) #ANNA

imieMale = imie1.lower()
print(imieMale) #anna

#sprawdzamy zawartosci
nazowsko = ""
print(nazowsko.isalpha()) #False

print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #True or False

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 +" " + text2)

#wyświetlenie łańcucha znaków

#wszystkie wersje Pythona
text = "%s %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisane danych
rok = 2019
miesiac = "kwiecien"
dzien = 1

print("\nData:", end="")
print(dzien, miesiac, rok, sep="-")

