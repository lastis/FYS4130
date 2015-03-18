import os

# First run. p = 0.5
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_5.cpp -O3')
os.system('./a.out x1_5_1.dat 0.5')

# Second run. p = 0.9
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_5.cpp -O3')
os.system('./a.out x1_5_2.dat 0.9')
