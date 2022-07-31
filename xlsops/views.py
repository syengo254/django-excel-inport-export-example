from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

import django_excel as excel

from xlsops.models import Category, Product

# Create your views here.


def index(request):
    return HttpResponse('<h1>Welcome to excel import export app!</h1>')


def import_data(request):
    if request.method == "GET":
        return render(request, 'import_view.html', {})
    else:
        file = request.FILES.get("file")
        if file:
            def product_initializer(row):
                c = Category.objects.filter(name__icontains=row[1])[0]
                row[1] = c
                return row

            file.save_book_to_database(
                models=[Category, Product],
                initializers=[None, product_initializer],
                mapdicts=[
                    ["name"],
                    {"product_name": "name", "category_name": "category", "price": "price"},
                ]
            )

            context = {
                "products": Product.objects.all(),
            }

            return render(request, "import_success.html", context)
        else:
            return HttpResponseBadRequest('No file received')

def export_data(request):
    export_obj = request.GET.get('obj', None)

    if export_obj:
        format = request.GET.get('format', 'xls')
        model = Category if export_obj == "categories" else Product

        # return HttpResponse(f"You requested object [{export_obj}] in {format} format.")
        return excel.make_response_from_a_table(model, format, file_name=f"{export_obj}_sheet")
    else:
        return render(request, 'export_view.html', {})
