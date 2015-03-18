import os

# First run. p = 0.5
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2.cpp -O3')
os.system('./a.out x1_1_1.dat 0.5')

# Second run. p = 0.1
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2.cpp -O3')
os.system('./a.out x1_1_2.dat 0.1')

# Third run. p = 0.01
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2.cpp -O3')
os.system('./a.out x1_1_3.dat 0.01')
