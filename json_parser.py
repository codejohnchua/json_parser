from json_lexer import JSONLexer
import ply.yacc as yacc

class JSONParser:
    def __init__(self):
        # Create JSON lexer 
        self.json_lexer = JSONLexer()

        # Build lexer
        self.json_lexer.build()
        self.tokens = self.json_lexer.tokens

        # Create parser
        self.json_parser = yacc.yacc(module=self, start='start')
        return
    
    def parse(self, data: str) -> int:
        try:
            print(self.json_parser.parse(data))
            return 0
        except SyntaxError as e:
            print("Syntax error: " + str(e))
            return 1

    # Error rule for syntax errors
    def p_error(self, p) -> None:
        raise SyntaxError(p)
        
    def p_start(self, p) -> None:
        '''
        start : object
        '''
        pass
    
    def p_object(self, p) -> None:
        '''
        object : LCURLYBRACKET pairs RCURLYBRACKET
        '''
        pass
    
    def p_pairs(self, p) -> None:
        '''
        pairs : empty
        '''
        pass
    
    def p_empty(self, p) -> None:
        '''
        empty :
        '''
        pass
    
