a = "a";
b = "b";
c = 1.1;

string1 = 'b = {nome2} a = {nome1} c = {nome3: .2f}';
formato1 = string1.format( nome1 = a, nome2 = b, nome3 = c);

#OU pode ser assim tambem:
string2 = 'b = {1} a = {0} c = {2: .2f}';
formato2 = string2.format( a, b, c);
                          #0, 1, 2

print(formato1, formato2);

