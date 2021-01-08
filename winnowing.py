""" Implemented using the paper https://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf 
Schleimer, Saul, Daniel S. Wilkerson, and Alex Aiken. 
"Winnowing: local algorithms for document fingerprinting." 
Proceedings of the 2003 ACM SIGMOD international conference on Management of data. 2003.

Example text: adorunrunrunadorunrun
"""

import hashlib

# Define the kind of hash function to use
def hash_fun(text):
    hs = hashlib.sha1(text.encode("utf-8"))
    hs = hs.hexdigest()[-4:]
    hs = int(hs, 16)
    return hs


# Get kgrams from a given string
# For example: abcde,3 -> abc bcd cde
def kgrams(text, n):
  text = list(text)
  return zip(*[text[i:] for i in range(n)])


# Get hashvalues from kgrams with 0-base positional information
def do_hashing(kgrams):
    hashlist = []
    for i,kg in enumerate(list(kgrams)):
        ngram_text = "".join(kg)
        hashvalue = hash_fun(ngram_text)
        hashlist.append((hashvalue, i))
    return hashlist


# Apply sliding window to list of hashes
def sl_window(hashes, n):
    return zip(*[hashes[i:] for i in range(n)])


# Get the minimum value of sliding windows
def get_min(windows):
    result = []
    prev_min = ()
    for w in windows:
        # Find minimum hash and take rightmost occurence
        min_h = min(w, key=lambda x: (x[0], -x[1])) 

        # Only use hash if differs from previous min
        if min_h != prev_min:
            result.append(min_h)
        prev_min = min_h
    return result

# Apply winnowing algorithm on text
def winnowing(text, size_k, window_size):
    hashes = (do_hashing(kgrams(text,size_k)))
    return set(get_min(sl_window(hashes, window_size)))


# Get similarity using winnowing algorithm + jaccard distance
def winnowing_similarity(text_a, text_b, size_k = 5, window_size = 4):
    # Get fingerprints using winnowing
    w1 = winnowing(text_a, size_k, window_size)
    w2 = winnowing(text_b, size_k, window_size)

    # Calculate jaccard distance
    union = len(w1.union(w2))
    intersect = len(w1.intersection(w2))
    return intersect / union