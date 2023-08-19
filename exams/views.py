from django.shortcuts import render


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
