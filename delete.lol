1   1   2       1   1   1
0   1   2       1   1   1
1   1   2       1   1   1

2   2   3       1   1   1   
1   2   3       1   1   1
2   2   3       1   1   1

1.5   2   2     0.5 1   1
1.5   2   3     1.5 1   1
2     2   3     1   1   1

2   x   
1   y   2   x   
1   y  



НА точці Б Знаходимо мінімальні точки А і сусідів БС. Для кожної точки з А знаходимо перетин її сусідів АС з сусідами точки Б. серед цього перетину знаходимо мінімальне значення МА. Знаходимо суму різниць між МА і А. Якщо це значення більше за рівень води в Б -> зливаємо порівну всю воду в А. Якщо це значення менше -> Зливаємо скільки можна і починаємо спочатку.

1)Вибираємо наступну точку (перша - (0, 0))
1а)Знаходимо всіх її сусідів
2)Знаходимо точки з мінімальною висотою в її оточенні
3)Для кожної точки з 2) знаходимо перетин сусідів з 1а)
4)Шукаємо мінімальну різницю між точкою з 2) і точками з 3)
5)Знаходимо суму різниць
6)Якщо сума різниць більша за рівень води в 1), то всю воду з 1 порівну виливаємо в кожну точку з 2 і goto 1
7)Якщо сума різниць менша - виливаємо воду в точки, в яких різниця з 4 мінімальна і goto 2