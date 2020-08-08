from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import MyDiary

def add_diary(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            value = request.POST['value']
            
            new_diary = MyDiary.objects.create(name=request.user, title=title, value=value)
            return HttpResponseRedirect(reverse('diary:my_diary'))
        else:
            pass
        return render(request, 'diary/add_diary.html')
    else:
        return HttpResponseRedirect(reverse('home:not_login'))


def my_diary(request):
    if request.user.is_authenticated:
        diary = MyDiary.objects.filter(name=request.user).order_by('-date_add')

        if len(diary) == 0:
            message = 'You have 0 diary'
        else:
            message = None

        return render(request, 'diary/my_diary.html', {
            'diary': diary, 
            'message':message,
        }
        )
    else:
        return HttpResponseRedirect(reverse('home:not_login'))


def detail_my_diary(request, diary_id):
    if request.user.is_authenticated:
        try:
            diary = MyDiary.objects.get(pk=diary_id)

            if request.user != diary.name:
                massage = "this diary does not exist"
            else:
                massage = None

            if diary.status == False:
                status_massage = 'this diary was deleted'
            else:
                status_massage = None
            
            return render(request, 'diary/detail.html', {
                'diary': diary,
                'massage': massage,
                'status_massage': status_massage,
                }
            )

        except (KeyError, MyDiary.DoesNotExist):
            massage = "this diary does note exist"
            return render(request, 'diary/detail.html', {
                # 'diary': diary,
                'massage': massage,
                }
            )
    else:
        return HttpResponseRedirect(reverse('home:not_login'))


def delete_diary(request, diary_id):
    if request.user.is_authenticated:

        try:
            get_diary = MyDiary.objects.get(pk=diary_id)

            if request.user != get_diary.name:
                pass
            else:
                delete = get_diary.delete()

            return HttpResponseRedirect(reverse('diary:my_diary'))

        except (KeyError, MyDiary.DoesNotExist):
            return HttpResponseRedirect(reverse('diary:my_diary'))

    else:
        return HttpResponseRedirect(reverse('home:not_login'))


def edit_diary(request, diary_id):
    if request.user.is_authenticated:
    
        try:
            get_diary = MyDiary.objects.get(pk=diary_id)

            if request.user != get_diary.name or get_diary.status is False:
                message = 'this diary does not exist or was deleted'
            else: 
                message = None
                pass

            if request.method == "POST":
                title = request.POST['title']
                value = request.POST['value']
                get_diary.title = title
                get_diary.value = value
                get_diary.save()
                return HttpResponseRedirect(reverse('diary:my_diary'))
            else:
                pass

            return render(request, 'diary/edit.html', {
                'message': message,
                'diary': get_diary
            }
            )

        except (KeyError, MyDiary.DoesNotExist):
            return HttpResponseRedirect(reverse('diary:my_diary'))

    else:
        return HttpResponseRedirect(reverse('home:not_login'))