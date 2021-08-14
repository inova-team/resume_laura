from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings

# Create your views here.
from django.template.loader import get_template

# from category.models import Category
from landing.models import Article
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse, JsonResponse


def renderHome(request):
    article_list = Article.objects.all().order_by('-publication_date')[:3]
    context = {
        'title_page': 'Inicio',
        'article_list': article_list,
    }

    return render(request, 'landing/index.html', context)

def renderCustom(request,id):
    context = {
        'title_page': 'Inicio',
        'link':id
    }

    return render(request, 'landing/index.html', context)


def renderContactUs_email(request):
    data = {}
    if request.POST:

        try:
            name = request.POST['name']
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')

            subject = f'Mensaje de {name}'
            sender = 'kurosaki.ishigo3@gmail.com'
            recipients = ['kurosaki.ishigo3@gmail.com']  # [email]
            # send_mail(subject, message, sender, recipients, fail_silently=True)

            context = {
                'name': name,
                'email': email,
                'number': number,
                'message': message,
            }

            template = get_template('assets/body_email.html')
            content = template.render(context)
            email = EmailMultiAlternatives(subject, '', sender, recipients, cc=[email])
            email.attach_alternative(content, 'text/html')
            email.send()

            data['exito'] = 'Se envió el correo con éxito'

        except Exception as e:

            data['error'] = str(e)

        return JsonResponse(data)


def renderArticle(request):
    article_list = Article.objects.all().order_by('-publication_date')
    context = {
        'title_page': 'Lista de Artículos',
        'article_list': article_list,
    }
    return render(request, 'landing/article_list.html', context)


def article_detail(request, pk):
    article = Article.objects.filter(pk=pk).exists()
    if article:
        article = Article.objects.get(pk=pk)
        list_articles = Article.objects.all().exclude(pk=pk).order_by('-publication_date')[
                        0:3]
        author = "Diego"
        context = {
            'article': article,
            'list_articles': list_articles,
            'author': author
        }
        return render(request, "landing/article_detail.html", context)
    else:
        return redirect('home')
