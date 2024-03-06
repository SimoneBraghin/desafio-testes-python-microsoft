# Gravar testes usando unittest

import unittest

class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one string", "one string")
        


# Executar testes
    
if __name__ == '__main__':
    unittest.main()