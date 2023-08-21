from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

from trains.models import Train


# Create your views here.
class TrainsIndex(LoginRequiredMixin, View):
    #      LoginRequiredMixin 로그인 되어 있는지 확인하고 안되어 있으면 러그린 화면으로 가는 class
    #     login_url = '/login/'  # 로그인 페이지 URL 설정
    def get(self, request):
        user = request.user
        try:
            train = Train.objects.get(id_user=user.id)
        except ObjectDoesNotExist:
            train = Train()
        context = {'train': train}
        return render(request, 'trains/trains_setting.html', context)

    def post(self, request):
        user = request.user

        train_word_range = request.POST.get('train_word_range')
        train_word_count = request.POST.get('train_word_count')
        train_repeat = request.POST.get('train_repeat')
        train_seconds = request.POST.get('train_seconds')
        train_tts_play = request.POST.get('train_tts_play')
        train_data_dict = {
            'train_word_count': train_word_count,
            'train_repeat': train_repeat,
            'train_seconds': train_seconds,
            'train_tts_play': train_tts_play,
        }
        print(train_data_dict)
        try:
            train = Train.objects.get(id_user=user.id)
            TrainsUtil.train_save(train, train_data_dict)
        except ObjectDoesNotExist:
            train = Train()
            train.id_user = user
            TrainsUtil.train_save(train, train_data_dict)

        return render(request, 'trains/trains_start.html')


class TrainsStart(View):
    def get(self, request):
        return render(request, 'trains/trains_start.html')

    def post(self, request):
        return render(request, 'trains/trains_start.html')


class TrainsUtil:
    @staticmethod
    def train_save(train: Train, train_data_dict):
        train.train_word_count = train_data_dict['train_word_count']
        train.train_repeat = train_data_dict['train_repeat']
        train.train_seconds = train_data_dict['train_seconds']
        train.train_tts_play = train_data_dict['train_tts_play']
        train.save()
