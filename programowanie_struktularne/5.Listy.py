programowanie = ['Python', 'C#', 'JS', 'PHP', 'Java']

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print('Pierwszy język programowania: ' + pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatni = programowanie[-1]
print('Pierwszy język programowania: ' + ostatni)


#########
programowanie.append('R')
print('programowanie')


##################
ile = programowanie.count('Python')
print('Python występuje {ile} razy')


#ilość elementów

iloscElem = len(programowanie)
print('Ilość elementów w liście: ', end='')
print(iloscElem)

#łączenie listy

print('\n\n{programowanie}')
inneJezyki = ['c', 'c++']
print('Połączenie z innymi językami')
programowanie.extended(inneJezyki)
print(programowanie)

#wyczyszczenie listy

nowa = programowanie
print('Nowa lista: {nowa}')
nowa.clear()
print('Nowa lista po wyczyszczeniu: {nowa}')
print('Lista programowanie po wyczyszczeniu: {programowanie}')
