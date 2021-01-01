from plot import draw_plot
from similarity import Code
from plot import draw_plot

#94%
file_A = "./TESTFILES/coding_example_1.py"
file_B = "./TESTFILES/coding_example_2.py"

#99%
file_C = "./TESTFILES/1_2_1.py"
file_D = "./TESTFILES/1_2_2.py"

#85%
file_E = "./TESTFILES/basics_strings_1.py"
file_F = "./TESTFILES/basics_strings_2.py"


c1 = Code(file_A)
c2 = Code(file_B)
print("C1 and C2 similarity = %s (Blocks: %s / %s )" %(c1.similarity(c2), len(c1.blocks), len(c2.blocks)))


c3 = Code(file_C)
c4 = Code(file_D)
print("C3 and C4 similarity = %s (Blocks: %s / %s )" %(c3.similarity(c4), len(c3.blocks), len(c4.blocks)))


c5 = Code(file_E)
c6 = Code(file_F)
print("C5 and C6 similarity = %s (Blocks: %s / %s )" %(c5.similarity(c6), len(c5.blocks), len(c6.blocks)))


draw_plot(c3, c4)