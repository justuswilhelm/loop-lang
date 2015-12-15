from parsimonious.grammar import Grammar

grammar = Grammar(r"""
program = (assignment / loop / output)*

NAME = ~r"x\d+"
NUMBER = ~r"(?:[1-9]\d*)|0"
MINUS = "-"
PLUS = "+"
ASSIGNMENT = ":="
SEMICOLON = ";"
_ = ~"\s*"

assignment = NAME _ ASSIGNMENT _ (NAME _ ( "+" / "-" ) _)? NUMBER _ SEMICOLON _
output = NAME _ SEMICOLON _
loop = "LOOP" _ NAME _ "DO" _ program _ "END" _
""")
