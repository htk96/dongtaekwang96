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
        paginator = Paginator(words, 15)
        page_number = request.GET.get("page")
        word_list = paginator.get_page(page_number)
        context = {'word_list': word_list}
        return render(request, 'words/word_list.html', context)

    def post(self, request):
        return HttpResponse('<h1> Words Index Page POST</h1')


class WordInput(View):
    def get(self, request):
        return render(request, 'words/word_input.html')

    def post(self, request):
        input_word: str = request.POST.get('input_word')
        input_word = input_word.replace(" ", "").replace("\r", "").replace("\n", "")
        input_word_list = input_word.split(',')

        if input_word_list[len(input_word_list) - 1] == "":
            input_word_list.pop(len(input_word_list) - 1)

        daum_dict = DaumDict(input_word_list[0])
        daum_dict.is_get_detail_page()
        find_word_dict = daum_dict.get_word_dict()

        show_word_list = ''

        for index, word in enumerate(input_word_list):
            if index == 0:
                show_word_list += f'<b>[{word}]</b>'
                if index < len(input_word_list) - 1:
                    show_word_list += ", "
            elif index < len(input_word_list) - 1:
                show_word_list += f'{word}, '
            else:
                show_word_list += f'{word}'

        context = {'show_word_list': show_word_list, 'input_word_list': input_word_list, 'find_word_num': 0,
                   'find_word_dict': find_word_dict}
        return render(request, 'words/word_find.html', context)
