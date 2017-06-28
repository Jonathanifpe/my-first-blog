from django.shortcuts import render
from django.utils import timezone
# Como views.py e models.py estão no mesmo diretório podemos simplesmente usar . e o nome do arquivo (sem .py).
from .models import Post

# Create your views here.

def post_list(request):

    #Pegar a lista de posts que foram publicados
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #Retornar os posts publicados (passando o resultado para o template)
    return render(request, 'blog/post_list.html', {'posts': posts})
