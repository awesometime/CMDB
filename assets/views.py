from django.shortcuts import render
from django.shortcuts import HttpResponse,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from . import asset_handler

# Create your views here.
def index(request):
    # 从数据库 获取 数据,需要和model联系起来
    # 也需要和template联系起来
    assets = models.Asset.objects.all()
    
    
    
#     给数据库写入     设置对象的值
#     if request.method == "POST":                           # 从用户post中取数据
#             name = request.POST.get('name', '')            # 取不到，默认为空
#             tags = request.POST.get('tags', '')           
#             price = request.POST.get('price', '')            
            
#             asset01 = models.Asset()        # 取到数据后存入数据库
#             asset01.name = name
#             asset01.tags = tags
#             asset01.price = price
#             asset01.save() 
        
    # render()函数的第一个位置参数是请求对象（就是view函数的第一个参数），
    # 第二个位置参数是待渲染的模板。
    # 还可以有一个可选的第三参数，经常是locals()，一个字典，包含需要传递给模板的数据。
    # 最后render函数返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象。
    return render(request, 'assets/index.html', locals())


def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline / total * 100)
    o_rate = round(offline / total * 100)
    un_rate = round(unknown / total * 100)
    bd_rate = round(breakdown / total * 100)
    bu_rate = round(backup / total * 100)
    server_number = models.Server.objects.count()
    networkdevice_number = models.NetworkDevice.objects.count()
    storagedevice_number = models.StorageDevice.objects.count()
    securitydevice_number = models.SecurityDevice.objects.count()
    software_number = models.Software.objects.count()

    return render(request, 'assets/dashboard.html', locals())


def detail(request, asset_id):
    """
    以显示服务器类型资产详细为例，安全设备、存储设备、网络设备等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    # 获取数据     如果对象不存在则弹出Http404错误
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())

@csrf_exempt
def report(request):
    """
    通过csrf_exempt装饰器，跳过Django的csrf安全机制，让post的数据能被接收，但这又会带来新的安全问题。
    可以在客户端，使用自定义的认证token，进行身份验证。这部分工作，请根据实际情况，自己进行。
    :param request:
    :return:
    """
    if request.method == "POST":                           # 从用户post中取数据
        asset_data = request.POST.get('asset_data', '')    # 取不到，默认为空
        data = json.loads(asset_data)
        # 各种数据检查，请自行添加和完善！
        if not data:
            return HttpResponse("没有数据！")
        if not issubclass(dict, type(data)):
            return HttpResponse("数据必须为字典格式！")
        # 是否携带了关键的sn号
        sn = data.get('sn', None)
        if sn:
            # 进入审批流程
            # 首先判断是否在上线资产中存在该sn
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                # 进入已上线资产的数据更新流程
                update_asset = asset_handler.UpdateAsset(request, asset_obj[0], data)
                return HttpResponse("资产数据已经更新！")
            else:
                # 如果已上线资产中没有，那么说明是未批准资产，进入新资产待审批区，更新或者创建资产。
                obj = asset_handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有资产sn序列号，请检查数据！")


