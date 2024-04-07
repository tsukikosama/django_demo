from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import cc_type
import json
from django.core.serializers.json import DjangoJSONEncoder
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#获取资源
def demoget(request):
    one_entry = cc_type.objects.all()
    print(one_entry)
    return HttpResponse(one_entry)



def demogetval(request):
    ##获取get请求参数
    print(request.GET.get("id"))
    print(request.GET.get("name"))

    return HttpResponse(request.GET)

@csrf_exempt
def demopost(request):
    ##获取请求路径的参数
    # print(request.POST.get("id"))
    # print(request.POST.get("name"))
    ##获取request.body里面的数据
    # 获取请求的原始数据
    raw_data = request.body.decode("utf-8")
    # 将原始数据转换成Python字典
    v = json.loads(raw_data)
    print(v)
    ##获取字典属性
    print(v['type_name'])
    return HttpResponse(request.body)

###保存对象
def save(request):
    if(request.method == 'POST'):
        # 获取请求的原始数据
        raw_data = request.body.decode("utf-8")
        # 将原始数据转换成Python字典
        v = json.loads(raw_data)
        c = cc_type(id=v['id'], type_name=v['type_name'])
        c.save();
    return HttpResponse("保存成功")

###查询指定的对象
def getone(request):
    if request.method == 'GET':
        id = request.GET['id']
        ##filter 去查询按照调教查询
        type = cc_type.objects.filter(id=id);
        return HttpResponse(type)
        # def getbyid(self)

##删除指定对象
def deleteone(request):
    if request.method == 'POST':
        # 获取请求的原始数据
        id = request.GET.get("id");
        print(id)
        type = cc_type.objects.filter(id=id).delete();
        return HttpResponse(type)

##修改指定对象
def updateone(request):
    if request.method == 'POST':
        # 获取请求的原始数据
        raw_data = request.body.decode("utf-8")
        # 将原始数据转换成Python字典
        v = json.loads(raw_data)
        ##返回影响的行数
        row = cc_type.objects.filter(id=v['id']).update(
            type_name=v['type_name']
        )
    return HttpResponse(row)