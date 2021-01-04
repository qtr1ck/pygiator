from pygments import token
from re import search
from operator import itemgetter

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
        category = 'O'
        #category = t[1] # All remaining operators
    elif t[0] == token.Text and t[1] == '\n':
        category = 'L'
    else:
        category = None # Comments and other tokens

    return category



def get_cmap():

    clist = [
        [0, "rgb(255, 255, 255)"],[ord('B'), "rgb(255, 255, 255)"],
        [ord('B'), "rgb(224, 221, 9)"], [ord('C'), "rgb(224, 221, 9)"],
        [ord('C'), "rgb(199, 193, 16)"], [ord('F'), "rgb(199, 193, 16)"],
        [ord('F'), "rgb(8, 204, 28)"], [ord('I'), "rgb(8, 204, 28)"],
        [ord('I'), "rgb(189, 189, 189)"], [ord('K'), "rgb(189, 189, 189)"],
        [ord('K'), "rgb(250, 0, 0)"], [ord('L'), "rgb(250, 0, 0)"],
        [ord('L'), "rgb(19, 35, 212)"], [ord('N'), "rgb(19, 35, 212)" ],
        [ord('N'), "rgb(176, 0, 235)" ], [ord('O'), "rgb(108, 159, 161)"],
        [ord('O'), "rgb(108, 159, 161)"], [ord('S'), "rgb(176, 0, 235)"],
        [ord('S'), "rgb(130, 0, 121)"], [ord('V'), "rgb(130, 0, 121)"],
        [ord('V'), "rgb(230, 130, 48)"], [ord('W'), "rgb(230, 130, 48)"],
        [ord('W'), "rgb(211, 252, 157)"]
    ]


    max_ = max(clist,key=itemgetter(0))[0]
    min_ = min(clist,key=itemgetter(0))[0]
    converted = []

    for element in clist:
        converted.append([(element[0] - min_) / (max_ - min_), element[1]])


    return converted