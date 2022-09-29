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
1. Setelah pengguna mengisi dan mensubmit form, data diterima django dan di-bind ke form tersebut agar bisa ditampilkan ulang
2. Data dibershikan dan divalidasi
3. Apabila data invalid, tampilkan ulang form dan data beserta error message
4. Apabila data valid, lakukan hal-hal yang dibutuhkan (cth: save, kirim email, upload file, dll.). Data di-POST ke database
5. Arahkan pengguna ke halaman lain
6. Dengan melakukan save tadi, database sudah di-update sehingga halaman HTMl yang terkait akan menampilkan data baru saat dimuat ulang

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. membuat aplikasi baru dengan perintah.
```
 python manage.py startapp todolist
```

2. Menambahkan todolist ke INSTALLED_APPS di file settings.py dalam folder project_django.

3. menambahkan routing di urls.py pada folder todolist dan folder project_django.

4. Membuat class Task di models.py.

5. menciptakan fungsi-fungsi berikut di views.py: <br>
- show_todolist 
- register
- login_user
- logout_user
- create_task

6. menciptakan file-file berikut di folder templates aplikasi todolist: <br>
- todolist.html
- register.html
- login.html
- create_task.html

7. Menambahkan autentikasi untuk mengakses halaman todolist.

8. Menciptakan file forms.py di folder aplikasi todolist dan menambahkan class TaskForm disana.

9. Mengimplementasikan class TaskForm di fungsi create_task untuk menciptakan form

10. Menciptakan file admin.py di folder aplikasi todolist dan mendaftarkan class Task