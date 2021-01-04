from plot import draw_plot
from similarity import Code

# #94%
file_A = "./TESTFILES/coding_example_1.py"
file_B = "./TESTFILES/coding_example_2.py"

# #99%
file_C = "./TESTFILES/1_2_1.py"
file_D = "./TESTFILES/1_2_2.py"

#85%
file_E = "./TESTFILES/basics_strings_1.py"
file_F = "./TESTFILES/basics_strings_2.py"


f1 = open(file_A)
f2 = open(file_B)
c1 = Code(f1.read())
c2 = Code(f2.read())
print("C1 and C2 similarity = %s (Blocks: %s / %s )" %(c1.similarity(c2), len(c1.blocks), len(c2.blocks)))
f1.close()
f2.close()



f1 = open(file_C)
f2 = open(file_D)
c3 = Code(f1.read())
c4 = Code(f2.read())
print("C3 and C4 similarity = %s (Blocks: %s / %s )" %(c3.similarity(c4), len(c3.blocks), len(c4.blocks)))
f1.close()
f2.close()


f1 = open(file_E)
f2 = open(file_F)
c5 = Code(f1.read())
c6 = Code(f2.read())
print("C5 and C6 similarity = %s (Blocks: %s / %s )" %(c5.similarity(c6), len(c5.blocks), len(c6.blocks)))
f1.close()
f2.close()

b1 = c1.blocks
b2 = c2.blocks

for b in b1:
    print("Similarity: %s  /  %s" %(b.similarity, b))
