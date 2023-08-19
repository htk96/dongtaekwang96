from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from words.crawling.daum_dict import DaumDict
from words.models import Word


# Create your views here.
class WordList(View):
    def get(self, request):
        words = Word.objects.all()
        paginator = Paginator(words, 20)
        page_number = request.GET.get("page")
        word_list = paginator.get_page(page_number)
        context = {'word_list': word_list}
        return render(request, 'words/index.html', context)

    def post(self, request):
        return HttpResponse('<h1> Words Index Page POST</h1')


class WordInput(View):
    def get(self, request):
        return render(request, 'words/word_input.html')

    def post(self, request):
        input_word = request.POST.get('input_word')
        daum_dict = DaumDict(input_word)
        if daum_dict.is_get_detail_page():
            get_word_dict = daum_dict.get_word_dict()
            return HttpResponse(f'<h1> Input Words : {get_word_dict} POST</h1')
