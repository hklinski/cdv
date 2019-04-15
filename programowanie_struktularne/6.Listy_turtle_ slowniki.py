#listy

programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
 #ile = programowanie.count('PHP')
 #print(f'ile razy jest PHP: {ile}'  )

#turtle
imiona = ('Julia', 'Anna', 'Tomek')
print(imiona)
print(type(imiona))
pierwszy = imiona[0]
print(pierwszy)

#słowniki
osoba = {
    'imie':  'Julia',
    'naziwsko': 'Kowalska',
    'wiek': 23
}

print(osoba)
print(type(osoba))
print(osoba['imie'])
print(osoba.keys())
print(osoba.get('wzrost', 'brak danych'))

'''
utwórz słownik i przypisz mu tzy imiona z klawiatury
wyświtl te dane na ekranie w formacie:
imie1:..
imie2:
imie3
'''
imie1 = input('\nPodaj imie: ')
imie2 = input('Podaj imie: ')
imie3 = input('Podaj imie: ')


osoba = {
'imie1':  imie1,
'imie2': imie2,
'imie3': imie3
}
print('imie1: ' + imie1)
print('imie2: ' + imie2 )
print('imie3: ' + imie3 )
