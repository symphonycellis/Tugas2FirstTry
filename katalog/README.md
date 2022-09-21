Link menuju aplikasi Heroku yang sudah di deploy : onitugas2.herokuapp.com/katalog

1) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![mvt - Frame 1](https://user-images.githubusercontent.com/112609270/190129626-77eac630-57f3-435b-8b24-44e95ef45eb2.jpg)
Model digunakan untuk manage dan query data  melalui objek python. Views digunakan untuk menerima HTTPRequest dari client dan mengembalikan HTTPResponse ke client. Template digunakan untuk menspesifikasi struktur dari dokumen output. 
Saat client memberi request, django framework menerima request dan melakukan submit request ke urls.py, urls.py bertindak seperti url mapper untuk redirect request ke views berdasarkan url yang direquest. Url mapper juga dapat menyocokan string yang sesuai melakukan pass ke views.py. Views.py kemudian melakukan accept request dan memproses instruction kemudian menyediakan HTTPResponse.
Saat client mengirimkan request yang berhubungan dengan interacting database. Maka request dikirim ke django, kemudian dilakukan redirected ke urls.py berdasarkan patternnya, dilanjutkan ke views.py, views.py melakukan identifikasi model untuk untuk berinteraksi dengan database. Lalu dilakukan read or write data ke models.py dan views juga menggunakan template untuk menyediakan user interface untuk client. Setelah pagenya sudah di generate dari template serta data, maka dikirimkan HTTPResponse ke client.

Source : https://www.youtube.com/watch?v=zhrLVCjNbyk

2) Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah alat untuk membantu menjaga dependencies yang diperlukan oleh berbagai project terpisah dengan membuat isolated python virual environment. Contoh case di mana kita memerlukan virtual environment adalah ketika kita sedang mengerjakan beberapa python project yang memerlukan versi django yang berbeda, kasus seperti inilah virtual environment diperlukan

Aplikasi web berbasis django tetap bisa dibuat tanpa menggunakan virtual environment. Akan tetapi, jika kamu mengerjakan beberapa project di machine yang sama, kemungkinan terjadinya conflict dependencies sangat besar. Misalnya, jika install django tanpa menggunakan virtual environment, maka django akan terinstall dalam project level, bukan system level.

Source : https://www.youtube.com/watch?v=HGQ3goOxrHQ, https://stackoverflow.com/questions/31263904/do-i-really-need-to-use-virtualenv-with-django

3) Jelaskan bagaimana cara kamu mengimplementasikan hal-hal di atas.
- Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
	
  Pengambilan data dari model yang diperlukan adalah nama, npm, serta list barang. Maka digunakan class untuk melakukan pengambilan data dari database yaitu from katalog.models import CatalogItem. Kemudian kita perlu menambahkan kode untu memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Setelah itu kita menambahkan context pada pengembalian fungsi render sehingga akhirnya data yang ada pada variable context tersebut akan ikut dirender oleh Django dan dapat memunculkan data pada page html.
def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'Name' : 'Symphony Cellis Zaana Saraaya',
        'StudentID' : '2106752060',
        'list_barang' : data_barang_katalog
    }
    return render(request, "katalog.html", context)

- Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py

Cara membuat routing untuk fungsi yang telah dibuat pada views.py adalah dengan menambahkan path('katalog/', include('katalog.urls')) pada urlspatterns didalam file urls.py

- Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

Data yang ditambahkan adalah nama, npm, serta detail barang. Sebelumyna di views.py kita sudah membuat dictionary yang berisi nama, npm, serta detai barang. Maka, di dalam file katalog.html kita bisa menambahkan {{Name}}, {{StudentID}}, kemudian detail list barang. Detail list barang yang diperlukan adalah nama, harga, stok, rating, deskripsi, serta url. Dapat dilakukan looping dari list_barang.

- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Deployment dilakukan dengan membuat aplikasi di heroku, kemudian dihubungkan ke github. Setelah itu, di dalam github secret kemudian actions, ditambahkan dua secret yaitu HEROKU_APP_NAME dengan isi nama aplikasi yang sebelumnya kita buat serta HEROKU_API_KEY yang berisi api key heroku kita yang didapat dari bagian account setting. Setelah itu di github kita dapat ke actions dan re-run jobs dan deployment akan berhasil.

