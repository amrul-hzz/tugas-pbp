# TUGAS 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming dapat mengerjakan beberapa hal sekaligus (secara parallel) sedangkan synchronous programming harus menunggu satu proses selesai baru memulai proses selanjutnya(secara serial). Asynchronous programming bagus diterapkan pada proses-proses yang tidak ada ketergantungan antara satu sama lain sedangkan synchronous programming bagus untuk proses-proses yang memiliki ketergantungan data (agar dapat dipastikan data yang benar ada saat dibutuhkan).

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah sebuah paradigma pemrograman dimana alur program tergantung dengan aksi dari user atau output tertentu. Contohnya, pada tugas ini, potongan kode yang menampilkan task baru hanya akan dijalankan saat user menekan tombol submit pada modal.

3. Jelaskan penerapan asynchronous programming pada AJAX.
Saat kita mengirim request ke server, biasanya (pada synchronous programming) kita harus menunggu reply dari server. Akan tetapi, pada asynchronous programming kita bisa langsung memproses halaman dan mengurus reply nanti saja saat reply tersebut tiba. Contoh penerapannya adalah kita bisa melihat data baru tanpa perlu memuat ulang seluruh halaman.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Menambahkan script AJAX ke base.html
- Menambahkan function show_todolist_json() di views.py untuk mengembalikan data dalam bentuk JSON
- Menambahkan AJAX GET ke script pada todolist.html 
