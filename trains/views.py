from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

from users.models import Config


# Create your views here.
class TrainsIndex(LoginRequiredMixin, View):
    #      LoginRequiredMixin 로그인 되어 있는지 확인하고 안되어 있으면 러그린 화면으로 가는 class
    #     login_url = '/login/'  # 로그인 페이지 URL 설정
    def get(self, request):
        user = request.user
        try:
            config = Config.objects.get(id_user=user.id)
        except ObjectDoesNotExist:
            config = Config()
        context = {'config': config}
        return render(request, 'trains/trains_setting.html', context)

    def post(self, request):
        user = request.user

        user_find_hint = request.POST.get('user_find_hint')
        config = Config()
        config.user_find_hint = user_find_hint
        config.id_user = user
        config.save()

        train_word_count = request.POST.get('train_word_count')
        train_repeat = request.POST.get('train_repeat')
        train_seconds = request.POST.get('train_seconds')
        train_tts_play = request.POST.get('train_tts_play')
        config_data_dict = {
            'train_word_count': train_word_count,
            'train_repeat': train_repeat,
            'train_seconds': train_seconds,
            'train_tts_play': train_tts_play,
        }
        print(config_data_dict)
        try:
            config = Config.objects.get(id_user=user.id)
            TrainsUtil.config_save(config, config_data_dict)
        except ObjectDoesNotExist:
            config = Config()
            config.id_user = user
            TrainsUtil.config_save(config, config_data_dict)

        return render(request, 'trains/trains_start.html')


class TrainsStart(View):
    def get(self, request):
        return render(request, 'trains/trains_start.html')

    def post(self, request):
        return render(request, 'trains/trains_start.html')


class TrainsUtil:
    @staticmethod
    def config_save(config: Config, config_data_dict):
        config.train_word_count = config_data_dict['train_word_count']
        config.train_repeat = config_data_dict['train_repeat']
        config.train_seconds = config_data_dict['train_seconds']
        config.train_tts_play = config_data_dict['train_tts_play']
        config.save()
