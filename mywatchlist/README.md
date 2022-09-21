Nama    : Amanda Nurul Izzah
<br>
NPM     : 2106634080
<br>
Kelas   : C
<br>

Tautan aplikasi Heroku: https://heroku-exercise-amrul-hzz.herokuapp.com/mywatchlist/

# Perbedaan antara JSON, XML, dan HTML
HTML digunakan untuk memberi struktur kepada halaman web sedangkan JSON dan XML merupakan sintaks untuk penyimpanan dan pertukaran data. Perbedaan antara JSON dan XML di antara lain adalah:
- JSON mengambil JSON string, XML mengambil dokumen XML
- JSON menggunakan JSON.parse() untuk mengurai data, XML menggunakan XML DOM untuk meng-loop dokumen

# Kenapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena kita memerlukan cara untuk bertukar data antar platform. Data yang kompleks dapat ditulis dalam JSON atau XML sehingga dapat dimengerti oleh berbagai API. 

# Pengimplementasian tugas 3
1. Ciptakan django-app bernama mywatchlist 
``` python manage.py startapp mywatchlist ```

2. Buka settings.py di folder project_django. Daftarkan mywatchlist ke proyek Django dengan menambakannya ke variabel INSTALLED_APPS
3. Buka models.py di folder mywatchlist. Tambahkan class BarangMywatchlist
4. Lakukan migrasi
``` python manage.py makemigrations ```
``` python manage.py migrate ```
5. Di folder mywatchlist, buat folder baru bernama fixtures. Dalam fixtures, tambahkan file initial_mywatchlist_data.json
6. Buka views.py di folder mywatchlist. Buat tiga fungsi, masing-masing untuk mengembalikan data dalam bentuk HTML, JSON, dan XML
7. Di folder mywatchlist, buat folder baru bernama templates. Dalam templates, tambahkan file baru bernama mywatchlist.html
8. Di folder mywatchlist, buat file baru bernama urls.py. Ciptakan routing terhadap fungsi-fungsi di views.py
9. Pada folder project_django, daftarkan aplikasi mywatchlist ke urls.py dengan menambahkannya ke urlpatterns
10. Git add, commit, push untuk deploy (deployment sudah dilakukan pada tugas sebelumnya) 

# Screenshot Postman
HTML
![show_watchlist_html](https://github.com/amrul-hzz/tugas-pbp/blob/main/mywatchlist/HTML_local.png)
![show_watchlist_html_1](https://github.com/amrul-hzz/tugas-pbp/blob/main/mywatchlist/HTML_heroku.png)

JSON
![show_watchlist_json](https://github.com/amrul-hzz/tugas-pbp/blob/main/mywatchlist/JSON_local.png)
![show_watchlist_json_1](https://github.com/amrul-hzz/tugas-pbp/blob/main/mywatchlist/JSON_heroku.png)

XML
![show_watchlist_xml](https://github.com/amrul-hzz/tugas-2-pbp/blob/main/mywatchlist/XML_local.png)
![show_watchlist_xml_1](https://github.com/amrul-hzz/tugas-2-pbp/blob/main/mywatchlist/XML_heroku.png)


