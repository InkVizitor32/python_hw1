# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, end =' ' )
            if -x*-z*-y==0:
                print('false')
            else:
                print('true')