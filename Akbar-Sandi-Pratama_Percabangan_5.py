<<<<<<< HEAD
# nama: Akbar Sandi Pratama
# kelas: XI TKJ 1
# nomor absen: 3
# soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa bedasarkan nilai tugas dan ujian
nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

if nilai_tugas > 70 and nilai_ujian > 60:
    status = "Lulus"
else:
    status = "Gagal"

=======
# nama: Akbar Sandi Pratama
# kelas: XI TKJ 1
# nomor absen: 3
# soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa bedasarkan nilai tugas dan ujian
nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

if nilai_tugas > 70 and nilai_ujian > 60:
    status = "Lulus"
else:
    status = "Gagal"

>>>>>>> f66a993b557c0da32b08c24847eccc1df0be71b2
print(f"Hasil: {status}")