data = {
    "programlama": "programlama kategorisine ait kurslar",
    "web-gelistirme": "webgeliştirme kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar",
    "backend": "backend kategorisine ait kurslar",    
}

def categories_processor(request):
    return {
        'categories': list(data.keys())
    }

