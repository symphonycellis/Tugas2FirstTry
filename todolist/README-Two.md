# Tugas 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Asynchronus Programming : Dalam menjalankan program, bisa dijalankan secara serentak (tidak perlu mengantri)
- Synchronus Programming : Dalam menjalankan program, dilakukan secara sekuensial (program dijalankan berdasarkan antrian)

Source : https://community.algostudio.net/memahami-synchronous-dan-asynchronous-dalam-pemrograman/#:~:text=Asynchronous%20adalah%20proses%20jalannya%20program,lama%20proses%20suatu%20fungsi%20synchronous%20.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event driven programming adalah ketika jalannya program itu berdasarkan event yang dilakukan oleh user.
Contoh penerapan di tugas ini adalah ketika user menambahkan task, maka akan muncul pop up modal.

Source : http://www.myspsolution.com/news-events/solace-event-driven/

## Jelaskan penerapan asynchronous programming pada AJAX.
Contohnya adalah jika kita menambahkan task maka tidak perlu dilakukan reload, dengan AJAX maka akan automatis tertambah.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### AJAX GET
### 1) Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
- Menambahkan di views.py
``` 
@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')
```
### 2) Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
- Menambahkan di urls.py di urlpatterns
```
path('json/',show_json,name="show_json"),
```
### 3) Lakukan pengambilan task menggunakan AJAX GET.
- Menambahkan di todolist.html
```
$.get("http://localhost:8000/todolist/json", function(data) {
     for (i=0;i<data.length;i++){
        $(".grid-container").append(`<div class="card text-bg-primary mb-3" style="max-width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">${data[i].fields.title}</h5>
            <p class="card-text">${data[i].fields.date}</p>
            <p class="card-text">${data[i].fields.description}</p>
          </div>`)
      }
    });
```
### AJAX POST
### 1) Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
- Dari modal bootstrap, ditambahkan ke todolist.html button ini
```
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Add task</button>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">New To Do</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="recipient-name" class="col-form-label">To Do:</label>
              <input type="text" class="form-control" id="field_title">
            </div>
            <div class="mb-3">
              <label for="message-text" class="col-form-label">Description:</label>
              <textarea class="form-control" id="field_desc"></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" id="msg" data-bs-dismiss="modal">Add</button>
        </div>
      </div>
    </div>
  </div>
```
### 2) Buatlah view baru untuk menambahkan task baru ke dalam database.
- Menambahkan di views.py
```
@csrf_exempt
def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.date.today()
        user = request.user
        todo = Task.objects.create(title=title, description=description, date=date, user=user)

        result = {
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'date':todo.date,
            },
            'pk':todo.pk
        }
        return JsonResponse(result)
```
### 3) Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
- Menambahkan di urlpatterns di urls.py
```
path('add/', add_todolist, name='add_todolist'),
```
### 4) Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
- Menambahkan ke todolist.html 
```
$("#msg").click(function(){
  $.post("/todolist/add/", {
    title : $('#field_title').val(),
    description: $('#field_desc').val()},
    function (result) {
      $(".grid-container").append(`<div class="card text-bg-primary mb-3" style="max-width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">${result.fields.title}</h5>
            <p class="card-text">${result.fields.date}</p>
            <p class="card-text">${result.fields.description}</p>
          </div>`)
      $('#field_title').val(''),
      $('#field_desc').val('')
    }
    ) 
  })
```
- Menyesuaikan ke modal yang telah dibuat
### 5) Tutup modal setelah penambahan task telah berhasil dilakukan.
- Button di atur seperti ini, ditambahkan data-bs-dismiss="modal"
```
<button type="button" class="btn btn-primary" id="msg" data-bs-dismiss="modal">Add</button>
```
### 6) Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.