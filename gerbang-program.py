# __main__ adalah top level dari environment

# __name__ == __main__

# __name__ pada file program utama
# import package_main
import fungsi
print(f'nilai __name__ pada gerbang-program.py = {__name__}')
# __name__ pada file program eksternal


def fungsi_tambah(a: int, b: int) -> int:
    return a+b


if __name__ == '__main__':
    angka1 = 4
    angka2 = 5
    hasil = fungsi_tambah(angka1, angka2)
    print(f'hasil dari penjumlahan {angka1} dan {angka2} adalah {hasil}')
