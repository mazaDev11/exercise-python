import numpy as np

# Cobb Douglas function
def cobb_douglas(A, K, L):
    return A * (K ** 0.3) * (L ** 0.7)

A_values = np.arange(1, 2.1, 0.1)
K_values = np.arange(1, 2.1, 0.1)
L_values = np.arange(1, 2.1, 0.1)

results = []

for A in A_values:
    for K in K_values:
        for L in L_values:
            F = cobb_douglas(A, K, L)
            results.append((A, K, L, F))
            print(f"A={A:.1f}, K={K:.1f}, L={L:.1f}, F={F:.2f}")


from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(['A', 'K', 'L', 'F'])

for row in results:
    ws.append(row)

wb.save('homeWork2/results.xlsx')