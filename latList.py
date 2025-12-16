#List python
#Penggunaan metode-metode bawaan Array

#daftar dengan nama mahasiswa
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]

#index untuk menampilkan item mahasiswa pada daftar
print(mahasiswa[0])
print(mahasiswa[1])
print(mahasiswa[2])
print(mahasiswa[3])
print(mahasiswa[4])
print(mahasiswa[5])
#gunakan Append  untuk menambahkan nama mahasiswa
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.append("Fadila")
print(mahasiswa)
#gunakan Insert untuk menyisipkan atau mengganti nama mahasiswa
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa[2]= "Sefila"
print(mahasiswa)
#gunakan Remove untuk menghapus nama mahasiswa dari list
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.remove("Nita")
print(mahasiswa)
#gunakan Pop untuk menghapus nama mahasiswa tertentu
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.pop(2)
print(mahasiswa)
#gunakan Count untuk menghitung berapa kali nama mahasiswa yang sama akan muncul
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul", "Vira"]
print(mahasiswa.count("Vira"))
#gunakan Sort untuk mengurutkan daftar berdasarkah abjad
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.sort()
print(mahasiswa)
#gunakan Reverse untuk membalikan urutan daftar
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.reverse()
print(mahasiswa)
#gunakan Len untuk menghitung jumlah mahasiswa pada list daftar
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
print(len(mahasiswa))
#gunakan Extend untuk memperpanjang list
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
teman = ("Fadila", "Sefila")
mahasiswa.extend(teman)
print(mahasiswa)
#gunakan Clear untuk menghapus semua elemen dari daftar
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.clear()
print(mahasiswa)
#gunakan copy untuk mengembalikan salinan daftar/menyalin daftar
mahasiswa = ["Vira", "Nita", "Zaena", "Almy", "Laras", "Faiqatul"]
mahasiswa.copy()
print(mahasiswa)