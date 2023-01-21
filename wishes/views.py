from django.http import HttpResponse,JsonResponse
from django.middleware.csrf import get_token
from random import shuffle
from .models import Wish
import json


def wishQuerySet2Array(querySet):
    res={}
    querySet = list(querySet)
    shuffle(querySet)
    for cnt, wish in enumerate(querySet):
        cnt += 1
        res[f'wisher{cnt}']=wish.wisher
        res[f'wishID{cnt}']=wish.id
        res[f'wishContent{cnt}']=wish.wishContent
        res[f'reward{cnt}']=wish.reward
        res[f'isRealized{cnt}']=wish.isRealized
    res['wishCnt'] = len(querySet)
    return res

def getAllWishes(request):
    wishes=Wish.objects.filter()
    return HttpResponse(json.dumps(wishQuerySet2Array(wishes)))

def getSingleWish(request,wishId):
    wishes=Wish.objects.filter(id=wishId,isRealized=False)
    return HttpResponse(json.dumps(wishQuerySet2Array(wishes)))

def addNewWish(request):
    da=json.loads(request.body)
    # print(da)
    if (len(da['wisher'])>0 and len(da['wishContent'])>0 and len(da['reward'])>0):
        Wish.objects.create(wisher=da['wisher'], wishContent=da['wishContent'],reward=da['reward'], isRealized=False)
        return HttpResponse('success')
    else:
        return HttpResponse('failed')

def confirmWish(request,wishID):
    wishes=Wish.objects.filter(id=wishID,isRealized=False)
    if(wishes.count()!=1):
        return HttpResponse('failed')
    else:
        for wish in wishes:
            wish.isRealized=True
            wish.save()
        return HttpResponse('success')

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'token': csrf_token})
