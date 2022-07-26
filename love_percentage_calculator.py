name1=input('enter your first love name')
name2=input('enter your secound love name')
L=name1.count('L') + name2.count('L') + name1.count('l') + name2.count('l')
O=name1.count('O') + name2.count('O') + name1.count('o') + name2.count('o')
V=name1.count('V') + name2.count('V') + name1.count('v') + name2.count('v')
E=name1.count('E') + name2.count('E') + name1.count('e') + name2.count('e')

T = name1.count('T') + name2.count('T') + name1.count('t') + name2.count('t')
R = name1.count('R') + name2.count('R') + name1.count('r') + name2.count('r')
U = name1.count('U') + name2.count('U') + name1.count('u') + name2.count('u')
E = name1.count('E') + name2.count('E') + name1.count('e') + name2.count('e')

a = (str(L+O+V+E) + str(T+R+U+E))
if(int(a) > 100):
     print("100% YOU ARE MADE FOR EACH OTHER")
else:
    print(str(L+O+V+E) + str(T+R+U+E) + "%")
