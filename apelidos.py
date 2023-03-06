'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    nomes.sort(key=lambda x: (len(x.split())-1, x))
    return nomes

##
# Main function of the Python program.
#
##


def main():
    print("<h3>apelidos</h3>")
    nomes = ["Jose Carlos Bacelar Almeida",
             "Maria Joao Frade",
             "Jose Bernardo Barros",
             "Jorge Manuel Matos Sousa Pinto",
             "Manuel Alcino Pereira Cunha",
             "Xico Esperto"]
    print("in:",nomes)
    print("out:",apelidos(nomes))


##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

import unittest


class apelidosTest(unittest.TestCase):
    
    def test_apelidos_1(self):
            self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])

    def test_apelidos_2(self):
            self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])

            
if __name__ == '__main__':
    main()
    unittest.main()