import ply.lex as lex

class JSONLexer:
    # List of token names. This is always required.
    tokens = (
        'LCURLYBRACKET',
        'RCURLYBRACKET'
    )

    # Regular expression rules for simple tokens.
    t_LCURLYBRACKET = r'\{'
    t_RCURLYBRACKET = r'\}'

    # Error handling rule.
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        pass

    # Build the lexer.
    def build(self, **kwargs) -> None:
        self.lexer = lex.lex(module=self, **kwargs)
        pass