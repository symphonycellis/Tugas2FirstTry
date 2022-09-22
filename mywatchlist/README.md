 Link deploy : onitugas2.herokuapp.com/mywatchlist
 
 Jelaskan perbedaan antara JSON, XML, dan HTML!
 JSON, singkatan dari JavaScript Object Notation, adalah suatu format ringkas pertukaran data komputer. Formatnya berbasis teks dan terbaca-manusia serta digunakan untuk merepresentasikan struktur data sederhana dan larik asosiatif.
 XML adalah XML adalah bahasa markup untuk keperluan umum yang disarankan oleh W3C untuk membuat dokumen markup keperluan pertukaran data antar sistem yang beraneka ragam. XML merupakan kelanjutan dari HTML yang merupakan bahasa standar untuk melacak Internet.
 HTML adalah Hypertext Markup Language adalah bahasa markah standar untuk dokumen yang dirancang untuk ditampilkan di peramban internet. Ini dapat dibantu oleh teknologi seperti Cascading Style Sheets dan bahasa skrip seperti JavaScript dan VBScript.
 
 source : https://id.wikipedia.org/wiki/JSON , https://id.wikipedia.org/wiki/XML , https://id.wikipedia.org/wiki/HTML
 
 
 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 Diperlukan data delivery untuk mempermudah pengiriman data yang menggunakan berbagai platform
 
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 Pertama saya menjalankan perintah startapp untuk membuat app baru bernama mywatchlist. Selanjutnya saya menambahkan melakukan routing dengan menambahkan mywatchlist pada installed_apps serta menambahkan path di file urls.py. Selanjtunya saya membuat class barangMyWatchList dengan isi hal-hal yang sesuai. Lalu saya membuat 10 object di initial_data_mywatchlist.json di folder fixtures yang saya buat Setelah itu saya melakukan loaddata initial_data_mywatchlist. Kemudian saya mengatur agar bisa diakses dengan bentuk cml, html, serta json. Setelah itu saya melakukan add, commit, lalu push melalui cmd. 
 
 Postman :
 ![image](https://user-images.githubusercontent.com/112609270/191664197-8b8c7c7f-dd0a-4a67-8acf-8490115894de.png)
![image](https://user-images.githubusercontent.com/112609270/191664176-213ee243-e312-4bcd-9610-2d7e8efb1d87.png)
![image](https://user-images.githubusercontent.com/112609270/191664151-f74b63ef-b0ad-45f9-b36c-5cf7ebb50348.png)
