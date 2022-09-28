Link app deploy : onitugas2.herokuapp.com/todolist

1) Apa kegunaan {% csrf_token %} pada elemen form ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

CSRF Token bersifat unik yang dibuat di server dan dikirim ke klien dalam bentuk HTTP Request. Fungsi CSRF Token adalah untuk mencegah CSRF attack sehingga attacker tidak dapat melakukan HTTP Request, jika tidak ada, maka attacker bisa masuk.

2) Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Bisa, berikut adalah contoh penerapannya.
```
<form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>To Do: </td>
                <td><input type="text" name="todo" placeholder="insert your to do" class="form-control"></td>
            </tr>             
            <tr>
                <td>Description: </td>
                <td><input type="text" name="description" placeholder="insert your description" class="form-control"></td>
            </tr>        
        </table>
        <input type="submit" name="submit" value="Add"/>
    </form>
```

Dapat dibuat method form. Lalu ditambahkan {% csrf_token %}. Di form dimasukkan tipe input dan name serta placeholder.

3) Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pengguna memasukkan data di form, server melakukan check apakah data yang di input sudah sesuai dengan aturan, kemudian data diarahkan ke views.py dan disimpan di database dan disimpan, selanjutnya data dapat diambil sehingga dapat muncul di page html.

4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

a. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.

Menjalankan di cmd di direktori yang sesuai python manage.py startapp todolist

b. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.

Menambahkan path di folder project_django file urls.py berupa
path('todolist/', include('todolist.urls')),

c. Membuat sebuah model Task

Di folder todolist, di file models.py dibuat class bernama Task yang memiliki atribut user, date, title, description.
User dengan memanfaatkan foreign key, date dengan tipe DateField, title dan description dengan tipe CharField.
```
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
```

d. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

Di folder todolist, di file views.py membuat fungsi register, login, dan logout
```
 def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')
	Kemudian membuat file register.html, login.html, logout.html di folder templates. Selanjutnya, dilakukan routing di urls.py di folder todolist dengan menambahkan 
path('register/', register, name='register'),
    	path('login/', login_user, name='login'),
    	path('logout/', logout_user, name='logout'),
di urlpatterns.
```
Serta dilakukan juga import setiap fungsinya.

e. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

Membuat fungsi show_todolist di views.py yang memuat dictionary dan key untuk data to do list
Membuat todolist.html di folder templates, untuk menampilkan username bisa menggunakan dict sebelumnya.
```
{% extends 'base.html' %}

 {% block content %}

  <h1>Assignment 4 PBP/PBD : To Do List</h1>

  <h5>Username : </h5>
  <p>{{username}}</p>

  <button><a href="{% url 'todolist:add_task' %}">Add task</a></button>
  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

  <table>
    <tr>
      <th>Date</th>
      <th>Task</th>
      <th>Description</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for todo in list_todolist %}
        <tr>
            <th>{{todo.date}}</th>
            <th>{{todo.title}}</th>
            <th>{{todo.description}}</th>
        </tr>
    {% endfor %}
  </table>

 {% endblock content %}
```

f. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

Membuat addtask.html di folder templates
```
{% extends 'base.html' %}

{% block meta %}
<title>Add To Do List</title>
{% endblock meta %}

{% block content %}

<div class = "create">

    <h1>Add To Do List</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>To Do: </td>
                <td><input type="text" name="todo" placeholder="insert your to do" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Description: </td>
                <td><input type="text" name="description" placeholder="insert your description" class="form-control"></td>
            </tr>
            
        </table>


        <input type="submit" name="submit" value="Add"/>
    </form>
</div>

{% endblock content %}
```

Menambahkan path di urls.py di urlspatterns
path('create-task/', add_task, name='add_task'),
serta melakukan import create-task juga

g. Membuat routing sehingga beberapa fungsi

Menambahkan ini di file urls.py
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
]
```

h. Melakukan deployment ke Heroku terhadap aplikasi

Menambahkan 2 secret yang mencangkup api key dan nama aplikasi.

i. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task
Melakukan register akun, kemudian login, menambahkan task sebanyak 3x 	diulang sebanyak 2x

