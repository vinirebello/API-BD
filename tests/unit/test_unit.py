from source import api_dao, database
import unittest

class TesteArtistas(unittest.TestCase):
    def setUp(self):
        self.bd = database()
        self.api = api_dao()
        
    def test_cria_artista(self):
        pass

        

if __name__ == '__main__':
    unittest.main()