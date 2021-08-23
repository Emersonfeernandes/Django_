from django.shortcuts import render
from .models import ProjetoFilmes
from .forms import UserForm

def homepage(request):
    return render(request=request, template_name="home.html", context={"Filmes" : ProjetoFilmes.objects.all})


def favorito(request):
    submitbutton = request.POST.get("submit")

    filme1 = str
    filme2 = str
    filme3 = str
    filme4 = str
    filme5 = str

    form = UserForm(request.POST or None)
    if form.is_valid():
        filme1 = form.Cleaned_data.get("Filme 1")
        filme2 = form.Cleaned_data.get("Filme 2")
        filme3 = form.Cleaned_data.get("Filme 3")
        filme4 = form.Cleaned_data.get("Filme 4")
        filme5 = form.Cleaned_data.get("Filme 5")

    context = {"form":form, "filme1":filme1, "filme2":filme2, "filme3":filme3, "filme4":filme4, "filme5":filme5
                , "submitbutton":submitbutton}

    return render(request=request, template_name="favoritos.html", context=context)
