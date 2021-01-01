from pygments.lexers import PythonLexer
from operator import itemgetter
from statistics import mean
from levensthein import lvs_distance
from categories import get_category
import numpy as np

# Hold tokens for a single block within own class instance
class Block(object):
    def __init__(self, tokens, similarity = 0, compared = False):
        self._similarity = similarity
        self._compared = compared
        self._tokens = tokens

    @property
    def similarity(self):
        return self._similarity

    @similarity.setter
    def similarity(self, s):
        self._similarity = s
    
    @property
    def compared(self):
        return self._compared

    @compared.setter
    def compared(self, v):
        self._compared = v

    @property
    def tokens(self):
        return self._tokens


    # OPERATOR OVERLOADS:
    #---------------------------------------------------------------------------
    # TODO: WHICH LEN TO RETURN?????
    def __len__(self):
        #total_len = 0
        #for t in self.tokens:
            #total_len += len(t[3])
        #return total_len
        return len(self.tokens)

    def __str__(self):
        return (''.join(str(t[0]) for t in self.tokens))


    # OBJECTMETHODS:
    #---------------------------------------------------------------------------

    #TODO : Performance -> Use other Levensthein implementation, Use Weights??
    def compare(self, other):
        # Get similarity comparing two blocks
        if (isinstance(other, Block)):
            ldis = lvs_distance(str(self),str(other))
            max_t_len = max(len(str(self)), len(str(other)))
            s_score = (1 - ldis/max_t_len) #Return similarity score

            return s_score

    # TODO: Restore linefeeds and whitespaces when creating clearstring?
    def clnstr(self):
        return (''.join(str(t[3].lower()) for t in self.tokens))

    def max_row(self):
        return max(self.tokens, key=itemgetter(1))[1]

    def max_col(self):
        return max(self.tokens, key=itemgetter(2))[2]




# Represent a files source code as tokens, also implements similarity check
class Code:
    def __init__(self, filename):
        self._blocks = []
        self._max_row = 0
        self._max_col = 0
        self.__tokenize(filename) # Generatore tokens from file
    
    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, b):
        self._blocks = b

    # Generate tokens for file
    def __tokenize(self, filename):
        file = open(filename, "r")
        text = file.read()
        file.close()
        lexer = PythonLexer() # Using pygments Python Lexer
        tokens = lexer.get_tokens(text)
        tokens = list(tokens) # Convert to tokens to list object
        result = []
        prev_c = '' # Remember previous category
        row = 0     # Remember position of row
        col = 0     # Remember position of column

        # Simplify tokens using categories and add additional coordinates
        for token in tokens:
            c = get_category(token)
            
            if (c != None):
                # Linefeed detected -> do not append to result but change position
                if c == 'L':
                    row = row + 1 #Increment line position
                    col = 0 # Set back column after linefeed

                # New block detected
                elif prev_c == 'L' and c != 'I' and result:
                    self.blocks.append(Block(result))
                    result = []

                if c != 'L':
                    result.append((c, row, col, token[1])) # Append result for single token
                    col += 1 #Increment column position
                    if col > self._max_col:
                        self._max_col = col
            prev_c = c
        self._max_row = row # Set max row for Tokens instance
        
        # Append last block if result not empty
        if result:
            self.blocks.append(Block(result))

    # Return numpy array representation of similarity
    def get_sim_array(self):
        data = np.zeros((self._max_row, self._max_col), dtype=float) #Initialize empty array
        
        for block in self.blocks:
            sim = block.similarity
            for t in block.tokens:
                data[t[1]][t[2]] = sim

        return data

    # Return numpy array representation of clearstrings
    def get_clnstr_array(self):
        data = np.zeros((self._max_row, self._max_col), dtype=object) #Initialize empty array
        
        for block in self.blocks:
            for t in block.tokens:
                data[t[1]][t[2]] = t[3]

        return data

    # Return numpy array representation of categories
    def get_ctg_array(self):
        data = np.zeros((self._max_row, self._max_col), dtype=int) #Initialize empty array
        
        for block in self.blocks:
            for t in block.tokens:
                data[t[1]][t[2]] = ord(t[0])

        return data


    # Set all blocks status to uncompared
    def _setUncompared(self):
        for block in self.blocks:
            block.compared = False


    # Find exact matches using stringcompare and annotate
    def __pre_process(self, other):
        other_blocks = other.blocks
        for block_a in self.blocks:
            for j,block_b in enumerate(other_blocks):
                if block_a.similarity == 1:
                    break
                if not block_b.compared:
                    if block_a.clnstr() == block_b.clnstr():
                        block_a.similarity = 1.0
                        other_blocks[j].compared = True

    # TODO: FIND A BETTER METHOD BACKTRACKING??
    # TODO: use difflib get_close_matches ??
    def __process_similarity(self, other):
        for block_a in self.blocks:
            if block_a.similarity < 1:
                best_score = 0
                index_best = 0
                for j,block_b in enumerate(other.blocks):
                    if not block_b.compared:
                        score = block_a.compare(block_b)
                        if score > best_score:
                            best_score = score
                            index_best = j
                block_a.similarity = best_score
                if best_score > 0:
                    other.blocks[index_best].compared = True

    # Calculate similarity score
    def __calculateSimScore(self):
        total_len = 0
        len_plagiat = 0
        for block in self.blocks:
            total_len += len(block)
            len_plagiat += len(block) * block.similarity
        return round((len_plagiat/total_len),2)

        #Using mean of block similarity:
        #similarity_list = []
        #for block in self.blocks:
        #    similarity_list.append(block.similarity)
        #return round((mean(similarity_list)),2)


    # Return similarity 
    def similarity(self, other):
        other._setUncompared()

        self.__pre_process(other)           # Do preprocessing step finding exact matches
        self.__process_similarity(other)    # Compare remaining blocks using levensthein distance on token categories
        return self.__calculateSimScore()