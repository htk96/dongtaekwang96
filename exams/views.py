from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

from trains.models import Train


class ExamsSetting(LoginRequiredMixin, View):
    #      LoginRequiredMixin 로그인 되어 있는지 확인하고 안되어 있으면 러그린 화면으로 가는 class
    #     login_url = '/login/'  # 로그인 페이지 URL 설정

    def get(self, request):
        user = request.user
        try:
            train = Train.objects.get(id_user=user.id)
        except ObjectDoesNotExist:
            train = Train()
        context = {'train': train}
        return render(request, 'exams/exams_setting.html', context)

    def post(self, request):
        user = request.user

        train_word_range = request.POST.get('train_word_range')
        exam_word_count = request.POST.get('exam_word_count')
        exam_seconds = request.POST.get('exam_seconds')
        exam_tts_play = request.POST.get('exam_tts_play')
        exam_difficulty = request.POST.get('exam_difficulty')
        train_data_dict = {
            'exam_word_count': exam_word_count,
            'exam_seconds': exam_seconds,
            'exam_tts_play': exam_tts_play,
            'exam_difficulty': exam_difficulty,
        }
        print(train_data_dict)
        try:
            train = Train.objects.get(id_user=user.id)
            ExamUtil.train_save(train, train_data_dict)
        except ObjectDoesNotExist:
            train = Train()
            train.id_user = user
            ExamUtil.train_save(train, train_data_dict)

        return render(request, 'exams/exams_start.html')


class ExamUtil:
    @staticmethod
    def train_save(train: Train, train_data_dict):
        train.exam_word_count = train_data_dict['exam_word_count']
        train.exam_seconds = train_data_dict['exam_seconds']
        train.exam_tts_play = train_data_dict['exam_tts_play']
        train.exam_difficulty = train_data_dict['exam_difficulty']
        train.save()


def home(request):
    return render(request, 'exams/home.html')


def Information_Modification(request):
    return render(request, 'exams/Information_Modification.html')


def Withdrawal(request):
    return render(request, 'exams/Withdrawal.html')


def Word_Practice(request):
    return render(request, 'exams/Word_Practice.html')


def Word_Practice_Set(request):
    return render(request, 'exams/Word_Practice_Set.html')


def Word_Test(request):
    return render(request, 'exams/Word_Test.html')


def Word_Test_History(request):
    return render(request, 'exams/Word_Test_History.html')


def Word_Test_Score(request):
    return render(request, 'exams/Word_Test_Score.html')


def Word_Test_Set(request):
    return render(request, 'exams/Word_Test_Set.html')
