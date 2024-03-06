# Gravar um teste de unidade com o módulo unittest
import unittest

# def str_to_bool(value):
#     true_values = ['y','yes']
#     false_values = ['no', 'n']

#     if value in true_values:
#         return True
#     if value in false_values:
#         return False

# class TestStrToBool(unittest.TestCase):

#     def test_y_is_true(self):
#         result = str_to_bool('y')
#         self.assertTrue(result)

#     def test_yes_is_true(self):
#         result = str_to_bool('Yes')
#         self.assertTrue(result)

# if __name__ == '__main__':
#     unittest.main()

# Executar os testes e identificar a falha

"""Execução: python test_exercise.py
    
Falha identificada:  na linha 22 não há "YES" como parte dos valores; 
por isso, retorna "None" como valor implícito"""

# Corrigir o bug e fazer com que os testes passem

# def str_to_bool(value):
#     value = value.lower()
#     true_values = ['y','yes']
#     false_values = ['no', 'n']

#     if value in true_values:
#         return True
#     if value in false_values:
#         return False
    
# class TestStrToBool(unittest.TestCase):

#     def test_y_is_true(self):
#         result = str_to_bool('y')
#         self.assertTrue(result)

#     def test_yes_is_true(self):
#         result = str_to_bool('Yes')
#         self.assertTrue(result)
    

# if __name__ == '__main__':
#     unittest.main()


# Adicionar novo código com testes

def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)
    
    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main()