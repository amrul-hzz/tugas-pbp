Nama    : Amanda Nurul Izzah
<br>
NPM     : 2106634080
<br>
Kelas   : C
<br>

Tautan aplikasi Heroku: https://heroku-exercise-amrul-hzz.herokuapp.com/todolist/

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF token adalah token yang digunakan untuk mencegah serangan CSRF. Token tersebut unik untuk setiap session. Tanpa token ini, orang selain pengguna bisa saja membuat request tanpa seizin pengguna. Tentu ini berbahaya karena kredensial pengguna dapat dieksploitasi.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, bisa. Di dalam class dari form tersebut, kita tambahkan field untuk tiap atribut yang ingin didaftarkan di form. Kemudian, isi dari field-field tersebut didapatkan menggunakan function cleaned_data.get(). Untuk field yang perlu diisi namun masih kosong, raise error.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.