# Tugas 5
[Link App To Do List](onitugas2.herokuapp.com/todolist)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Inline CSS
Deskripsi :
- Untuk tag html tertentu
- Memakai </style> untuk memberikan style ke suatu tag html

Kelebihan :
- Cocok untuk quickfix dan testing
- Request HTTP yang lebih kecil

Kekurangan :
- Harus diterapkan di setiap elemen

### Internal CSS
Deskripsi :
- Ditaruh di dalam head
- Class, ID bisa digunakan untuk merujuk pada kode CSS

Kelebihan :
- Change terjadi di 1 page
- html dan CSS bisa digunakan di file yang sama
- Class, ID bisa dugnakan oleh internal stylesheet

Kekurangan :
- Waktu akses website bertamnbah
- Tidak efisien jika ingin dipakai di banyak file

### Eksternal CSS
Deskripsi :
- Menghubungkan CSS ke file
- Perubahan pada file CSS memengaruhi keseluruhan website
- Menambahkan ini di head
```
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
<head>
```
Kelebihan : 
- CSS bisa digunakan di banyak halaman
- Size file html kecil

Kekurangan :
- Sampai file CSS selesai dipanggil, halaman tidak akan tertampil sempurna

<b>Source : https://www.hostinger.co.id/tutorial/perbedaan-inline-css-external-css-dan-internal-css </b>


## Jelaskan tag HTML5 yang kamu ketahui.
```<body> : Mendefinisikan body dari suatu dokumen
<button> : Membuat tombol yang bisa di klik
<div> : Menspesifikasi suatu bagian di dalam dokumen
<head> : Mendifisikan bagian head dari dokumen (contohnya title)
<h1> sampai <h6> : Untuk heading html
<p> : Untuk paragraf
<table> : Untuk mendefinisikan data table
<style> : Memasukkan informasi style
```
Source : https://www.tutorialrepublic.com/html-reference/html5-tags.php

##  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Type Selector
Memilih elemen berdasarkan nama tag
Contoh :
```
p {
    color: red;
}
```
dengan file html
```
<p> hi </p>
<div> ok </div>
````
Maka hi akan memiliki warna blue
- Class selector

Memilih elemen berdasarkan nama class
Contoh :
```
.blue {
  color: white;
  background: blue;
  }
```
```.,
<p> ok <b class="blue"> kalau </b> begitu </p>
```
Maka kalau akan memiliki warna background biru dan tulisan putih.

- ID Selector
Mirip dengan class selector namun hanya bisa digunakan untuk satu elemen
```
#header {
    background: teal;
    color: white;
    height: 100px;
    padding: 50px;
}

<header id="header">
    <h1>Selamat Datang di Website Saya</h1>
</header>
```

- Atribut Selector
Memiliki elemen berdasarkan atribut
```
input[type=text] {
    background: none;
    color: cyan;
    padding: 10px;
    border: 1px solid cyan;
}

<input type="text" placeholder="ketik sesuatu..." />
```
Source : https://www.petanikode.com/css-selektor/

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
### Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
```
Menambahkan <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous"> di head di file html.
Menambahkan <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script> di body di file html.
```

### Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
Menambahkan 
```
{% comment %} Add the data below this line {% endcomment %}
  <div class = "grid-container">
    {% for todo in list_todolist %}
      <div class="card text-bg-primary mb-3" style="max-width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">{{todo.title}}</h5>
          <p class="card-text">{{todo.date}}</p>
          <p class="card-text">{{todo.description}}</p>
        </div>
      </div>
      {% endfor %}
```
di todolist

### Membuat keempat halaman yang dikustomisasi menjadi responsive.
Saya menggunakan bootstrap yang sudah mendukung responsive web desain sehingga web bisa diatur secara dinamis sesuai dengan platformnya.

