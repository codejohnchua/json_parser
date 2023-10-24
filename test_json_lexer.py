from json_lexer import JSONLexer
import unittest

class TestJSONLexer(unittest.TestCase):
    def test_build(self):
        json_lexer = JSONLexer()
        try:
            json_lexer.build()
        except Exception:
            self.fail("JSONLexer.build() raised an Exception unexpectedly.")
        pass

if __name__ == '__main__':
    unittest.main()