from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama": "programlama kategorisine ait kurslar",
    "web-gelistirme": "webgeliştirme kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar",
    "backend": "backend kategorisine ait kurslar", 
}

def index(request):
    # list_items = ""

    # category_list = list(data.keys())
    
    # for category in category_list:
    #     redirect_url = reverse('courses_by_category', args=[category])
    #     list_items += f"<li><a href='{redirect_url}>{category}</a></li>"   
  
    return render(request, 'courses/index.html/')

def details(request, kurs_name):
    return HttpResponse(f"{kurs_name} detay sayfası")

def getCoursesByCategory(request, category_name): 
    try:
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {'category' : category_name, 'category_text': category_text})
    except:
        return HttpResponseNotFound("Kategori bulunamadı")


def getCoursesByCategoryById(request, categoy_id):
    category_list = list(data.keys())    
    if  (categoy_id < 1 or categoy_id > len(category_list)):
        return HttpResponseNotFound("Kategori bulunamadı")
    category_name = category_list[categoy_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    

    return redirect(redirect_url)


