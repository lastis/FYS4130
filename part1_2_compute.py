import os

# First run. p = 0.1
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2.cpp -O3')
os.system('./a.out x1_2_1.dat 0.1')

# Second run. p = 0.01
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2.cpp -O3')
os.system('./a.out x1_2_2.dat 0.01')
