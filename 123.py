first = input()
second = input()
third = input()
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else :
    print('Обнаружено', 0, 'равных между собой чисел')
