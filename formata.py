"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""
def formata(codigo):
    ind = 0
    i = 0
    l = len(codigo)
    final = ""
    newline = True
    for c in codigo:
        i += 1
        if c == ';':
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '{':
            ind += 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '}':
            final = final[:-2]
            ind -= 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == ' ' and newline:
            continue
        else:
            newline = False
            final += c
    return final
#def formata(codigo):
#    novaString = ' '.join(codigo.split())
#    print(novaString)
#    novaStr = ""
#    for i in range(len(novaString)):
#        if novaString[i] != '{' and novaString[i] != '}' and novaString[i] != ';':
#            novaStr += novaString[i]
#        elif novaString[i] == '{':
#            novaStr +=  '{'+'\n' + '  '   
#        elif novaString[i] == '}' and i != (len(novaString)-1):
#            novaStr +=  '\n'+'}'+'\n  '
#        elif novaString[i] == ';':
#            novaStr += ';'+'\n  '
#            
# 
#    novaStr += '}' 
#    return novaStr


##
# Main function of the Python program.
#
##

def main():
    print("<h4>formata</h4>")
    codigo = "int main() {int x;x=0;     x=x+1;}"
    print(formata(codigo))


##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

import unittest

class formataTest(unittest.TestCase):

    def test_formata_1(self):
            codigo = "int x;x=0;x=x+1;"
            self.assertEqual(formata(codigo),"int x;\nx=0;\nx=x+1;")

    def test_formata_2(self):
            codigo = "int main() {int x;x=0;     x=x+1;}"
            self.assertEqual(formata(codigo),"int main() {\n  int x;\n  x=0;\n  x=x+1;\n}")
            
            
if __name__ == '__main__':
    main()
    #unittest.main()