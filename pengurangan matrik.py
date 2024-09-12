def kurang_matriks(A, B):
    hasil = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return hasil

hasil_kurang = kurang_matriks(A, B)
print("Hasil Pengurangan Matriks:")
for baris in hasil_kurang:
    print(baris)
