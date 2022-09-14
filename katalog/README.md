## Tugas 2 PBP

Nama            : Amanda Nurul Izzah
<br>
NPM             : 2106634080
<br>
Kelas           : PBP-C
<br>
Link heroku app : https://heroku-exercise-amrul-hzz.herokuapp.com/ 
<br>

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html; 

![bagan](https://github.com/amrul-hzz/tugas-2-pbp/blob/main/images/bagan.png)

2. Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
Virtual environment menciptakan ruang terpisah untuk pengembagna suatu proyek. Ruang ini berisi library dan dependency yang digunakan proyek tersebut. Dengan memisahkan ruang seperti ini, pengembangan dua proyek tidak akan mencampuri satu sama lain. Sebenarnya bisa-bisa saja kita membuat aplikasi web tanpa virtual environment, namun jika ada bentrokan nanti kita akan susah sendiri. Oleh karena itu, menggunakan virtual environment adalah best practice.

3. Cara mengimplementasikan poin 1 sampai dengan 4 pada Tugas 2
   - Poin 1: membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
      Menambahkan fungshi show_katalog() pada views.py. fungsi ini menerima request, mengambil data berdasarkan model, dan mengembalikan context yang dapat ditampilkan pada halaman katalog.html.
   - Poin 2: membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
      Menambahkan path menuju show_katalog di urlpatterns di urls.py pada folder katalog. Kemudian, menambahkan file katalog.urls tersebut ke urlpatterns di urls.py pada folder project_django.
   - Poin 3: memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
      Menambahkan for loop untuk mencetak data.
   - Poin 4: melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
      Pertama-tama, tambahkan HEROKU_API_KEY dan HEROKU_APP_NAME dengan nilai-nilai yang sesuai ke action secrets repository GitHub. Kemudian, make migrations dan migrate. Add, commit, dan push perubahan ke repository GitHub. Setelah workflow sudah selesai di-run, aplikasi dapat dibuka melalui link Heroku-nya. 