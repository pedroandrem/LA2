'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    dic = {}
    for i in texto.split():
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            
    result = [a for a,b in sorted(dic.items(), key = lambda x: (-x[1], x[0]))]
    
    return result

def main():
    print("<h3>frequencia</h3>")
    texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    print("in:",texto)
    print("out:",frequencia(texto))

import unittest

class frequenciaTest(unittest.TestCase):
    
    def test_frequencia_1(self):
            self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])

    def test_frequencia_2(self):
            self.assertEqual(frequencia("ola"),['ola'])
            
if __name__ == '__main__':
    main()
    unittest.main()