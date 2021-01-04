from pygments import token
from re import search

# Categorize the tokens
def get_category(t):
    category = '' # represent category as single uppercase char

    #TODO: seperate variables and calls!
    #TODO: what to do with quotes?
    #TODO: Import Token?

    if t[0] == token.Name.Function:
        category = 'F' # Functions
    elif t[0] == token.Name:
        category = 'V' # Variables
    elif t[0] == token.Name.Builtin:
        category = 'B' # Builtin functions (range,sort ....)
    elif t[0] in token.Literal.Number:
        category = 'N' # Numbers
    elif t[0] in token.Literal.String and t[1] != '\'' and t[0] not in token.Literal.String.Doc:
        category = 'S' # Strings
    elif t[0] in token.Keyword:
        category = 'K' # Keywords
    elif t[0] == token.Text and (t[1] == '\t' or search(r'\s{2,}', t[1]) != None):
        category = 'I' # Indent
    elif t[0] == token.Operator.Word:
        category = 'W' # Operator words (in not ...)
    elif t[0] == token.Operator and (t[1] == '==' or t[1] == '!='):
        category = 'C' # Comparison
    elif t[0] == token.Operator or t[0] == token.Punctuation:
        category = t[1] # All remaining operators
    elif t[0] == token.Text and t[1] == '\n':
        category = 'L'
    else:
        category = None # Comments and other tokens

    return category