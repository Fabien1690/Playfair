from square import Square

tab_alphabet = dict(A=1, B=2, C=3, D=4, E=5,
                    F=6, G=7, H=8, I=9, J=10,
                    K=11, L=12, M=13, N=14, O=15,
                    P=16, Q=17, R=18, S=19, T=20,
                    U=21, V=22, X=23, Y=24, Z=25)

carre_test = Square(tab_alphabet)

tab_random = dict(A=24, B=6, C=18, D=16, E=3,
                  F=9, G=17, H=8, I=7, J=23,
                  K=2, L=19, M=21, N=11, O=10,
                  P=5, Q=25, R=15, S=4, T=20,
                  U=12, V=22, X=14, Y=1, Z=13)

carre_test2 = Square(tab_random)

print(carre_test2.print_tableau())

values = list(tab_random.values())
print(values)
values.sort()
print(values)
print(values == list(range(1, 26)))

# print(tab_random)

# print(carre_test.get_letters("B", "T"))
# print(carre_test.get_letters("T", "B"))
# print(carre_test.get_letters("M", "T"))
# print(carre_test.get_letters("M", "Y"))

# alphabet = np.array([['a', 'b', 'c', 'd', 'e'],
#          ['f', 'g', 'h', 'i', 'j'],
#          ['k', 'l', 'm', 'n', 'o'],
#          ['p', 'q', 'r', 's', 't'],
#          ['u', 'w' 'x', 'y', 'z']])

# tab_a = [['a'], ['b'], ['c'], ['d'], ['e'],
#          ['a'], ['b'], ['c'], ['d'], ['e'],
#          ['a'], ['b'], ['c'], ['d'], ['e'],
#          ['a'], ['b'], ['c'], ['d'], ['e'],
#          ['a'], ['b'], ['c'], ['d'], ['e']]
