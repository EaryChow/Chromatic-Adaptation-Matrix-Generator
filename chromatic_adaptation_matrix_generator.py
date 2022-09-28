import numpy as np
import colour

np.set_printoptions(suppress=True)
I_E = np.array([1, 1, 1])
I_D65 = np.array([0.95047, 1, 1.08883])
method = 'Bradford'
matrix = colour.adaptation.matrix_chromatic_adaptation_VonKries(I_E, I_D65, method)
print(matrix)
