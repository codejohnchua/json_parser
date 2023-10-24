from json_parser import JSONParser
import unittest

def read_file(filename: str) -> str:
    if not filename:
        raise ValueError('missing filename')
    with open(filename, 'r') as file:
        return file.read()

class TestJSONLexer(unittest.TestCase):
    def test_step1_valid(self):
        json_parser = JSONParser()
        data = read_file('tests/step1/valid.json')
        self.assertEqual(json_parser.parse(data), 0)
        pass

    def test_step1_invalid(self):
        json_parser = JSONParser()
        data = read_file('tests/step1/invalid.json')
        self.assertEqual(json_parser.parse(data), 1)
        pass
        
if __name__ == '__main__':
    unittest.main()