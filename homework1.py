"""
Задача 1
Креирајте 2 листи.
1. По колку елементи има секоја од листите?
2. Во првата листа додадете го 2 пати истиот елемент.
3. Избришете ги дупликатите од првата листа. Како изгледа сега листата?
4. На првата листа додадете и ја втората. Колку елементи имаме сега?
5. Сортирајте ја новата листа. Како изгледа сега?
"""
l1 = [5, 7, 6, 9, 8]
l2 = [99, 77, 66]
print(f'l1 = ', len(l1))
print(f'l2 = ', len(l2))
# l1 има 5, l2 има 3 елементи.

l1.append(33)
l1.append(33)
print(l1)
#додаден ист елемент два пати во првата листа.


l1 = set(l1)
l1 = list(l1)
print(l1)
# избришани дупликатите во l1.


l1.extend(l2)
print(l1)
print(f'l1 ima {len(l1)} elementi.')
# listata l2, dodadena na l1.


l1.sort()
print(f'l1 po sortiranjeto izgleda vaka:{l1}')
#sortiranje na l1

"""
Задача 2
Дадена е листата: my_list = [5, 10, 15, 20, 25]
1. Кој е вториот елемент во листата?
2. Додадете елемент со вредност 30 на крајот.
3. Додадете елемент со вредност 0 на почетокот.
4. Сортирајте ја листата од најголем до најмал.
5. Извадете подлиста од 2риот елемент до крај.
"""
my_list = [5, 10, 15, 20, 25]
print(f'Vtoriot element vo listata my_list e {my_list[1]}')
#Vtoriot element vo listata my_list e 10.

my_list.append(30)
#dodavanje na element so vrednost 30 na krajot

my_list.insert(0, 0)
print(my_list)
#element 0 na pocetokot na listata

my_list.sort(reverse=True)
print(my_list)
#sortiranje po opaganje

print(my_list[1:])
# Подлиста од 2риот елемент до крај.


"""
Задача 3
1. Креирајте листа која ќе има 10 елементи.
2. Направете функција која на влез ќе прима 2 броја. Направете ги следниве проверки:
    1. Дали првиот број е помал од вториот. Доколку не е испринтајте внесовте грешка броеви. 
    2. Дали броевите се позитивни цели броеви. Доколку не се испринтајте внесовте негативни броеви. 
    3. Дали вториот број е помал од должината на листата. Доколку не е испринтајте внесете помал број. 
3. Користејќи ги овие 2 броја, креирајте подлиста која ќе почнува со првиот индекс, а ќе завршува со последниот.
4. Проверете дали во подлистата го имаме бројот 6. 
"""
l3 = [4, 5, 'k', 'p', 9, 7, 65, 31, 12, 'v']
def prim():
    a = int(input('Vnesi broj: '))
    b = int(input('Vnesi vtor broj: '))
    if not a < b:
        print(f'Vnesovte greska broevi.')
    if a < 0 or b < 0:
        print('Vnesovte negativni broevi.')
    if not b < len(l3):
        print('Vnesete pomal broj.')
prim()


# proverka dali brojot 6 postoi vo podlistata
if 6 in podlista:
    print('Brojot 6 postoi vo podlistata.')
else:
    print('Brojot 6 ne postoi vo podlistata.')

"""
Задача 4
Даден е речникот: grades = {'Ангела': 90, 'Бојан': 85, 'Васил': 95, 'Гордан': 80, 'Даниела': 100}
1. Колку поени има Ангела?
2. Во пресметувањето на поени, се увидело дека имаме грешка кај Гордан. Сменете ги неговите поени во 75.
3. Додадете нов ученик Никола со 92 поени.
4. Бојан се отпишал, па избришете ги информациите за него.
5. Колку ученици имаме и како се викаат?
6. Извадете ги сите поени кои ги освоиле студентите.
"""
grades = {'Ангела': 90, 'Бојан': 85, 'Васил': 95, 'Гордан': 80, 'Даниела': 100}
#1. Колку поени има Ангела?
print(grades.get('Ангела'))

# Во пресметувањето на поени, се увидело дека имаме грешка кај Гордан. Сменете ги неговите поени во 75.
grades['Гордан'] = 75

#Додадете нов ученик Никола со 92 поени.
grades['Никола'] = 92
print(grades)

#Бојан се отпишал, па избришете ги информациите за него.
del grades['Бојан']
print(grades)

#Колку ученици имаме и како се викаат?
print(f'Imame {len(grades)} ucenici.')
print(grades.items())

#Извадете ги сите поени кои ги освоиле студентите.
print(grades.values())



"""
Задача 5
Даден е речникот:
book_dict = {
    'Mystery': ['The Girl with the Dragon Tattoo', 'Gone Girl', 'The Da Vinci Code'],
    'Romance': ['The Notebook', 'Pride and Prejudice', 'The Fault in Our Stars'],
    'Science Fiction': ['The Hunger Games', 'Ender\'s Game', 'Dune'],
    'Fantasy': ['The Lord of the Rings', 'Harry Potter and the Philosopher\'s Stone', 'A Game of Thrones'],
    'Classics': ['To Kill a Mockingbird', 'The Catcher in the Rye', 'Wuthering Heights']
}
1. Додадете ја книгата The Silence of the Lambs во жанрот Mystery.
2. Избришете ја книгата Enders Game.
3. Кои се сите жанрови за кои имаме информации?
4. Колку книги имаме во жанрот Fantasy?
5. Проверете дали ја имаме книгата The Lord of the Rings во Fantasy.

Напишете го кодот и како коментар одговорете ги прашањата.
Решенијата генерирани со ChatGPT нема да се валидни како решена домашна.
"""
book_dict = {
    'Mystery': ['The Girl with the Dragon Tattoo', 'Gone Girl', 'The Da Vinci Code'],
    'Romance': ['The Notebook', 'Pride and Prejudice', 'The Fault in Our Stars'],
    'Science Fiction': ['The Hunger Games', 'Ender\'s Game', 'Dune'],
    'Fantasy': ['The Lord of the Rings', 'Harry Potter and the Philosopher\'s Stone', 'A Game of Thrones'],
    'Classics': ['To Kill a Mockingbird', 'The Catcher in the Rye', 'Wuthering Heights']
}

# Додадете ја книгата The Silence of the Lambs во жанрот Mystery.
book_dict['Mystery'].append('The Silence of the Lambs')
print(book_dict)


#Избришете ја книгата Enders Game.
book_dict['Science Fiction'].remove('Ender\'s Game')
print(book_dict)


#Кои се сите жанрови за кои имаме информации?
print(book_dict.keys())

# Колку книги имаме во жанрот Fantasy?
print(f"Vo zanrot 'Fantasy' ima {len(book_dict['Fantasy'])} knigi.")

# Проверете дали ја имаме книгата The Lord of the Rings во Fantasy.
print(book_dict['Fantasy'].index('The Lord of the Rings'))