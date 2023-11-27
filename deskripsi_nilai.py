def grade(nilai):
    if nilai >= 80 and nilai <= 100:
        return 'A'
    elif nilai >= 65:
        return 'B'
    elif nilai >= 50:
        return 'C'
    elif nilai >= 35:
        return 'D'
    elif nilai >= 0 and nilai <= 34:
        return 'E'
    else:
        return 'Nilai Invalid'

nama = input('Masukkan nama mahasiswa: ')
nilai = int(input('Masukkan nilai mahasiswa: '))
deskripsi_nilai = grade(nilai)

print(f'Nama Mahasiswa: {nama} \nDeskripsi Nilai: {deskripsi_nilai}')