def tambah_matriks(A, B):
    hasil = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return hasil

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

hasil_tambah = tambah_matriks(A, B)
print("Hasil Penjumlahan Matriks:")
for baris in hasil_tambah:
    print(baris)
