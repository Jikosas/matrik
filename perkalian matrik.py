def kali_matriks(A, B):
    hasil = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return hasil

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

hasil_kali = kali_matriks(A, B)
print("Hasil Perkalian Matriks:")
for baris in hasil_kali:
    print(baris)
