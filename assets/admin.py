from django.contrib import admin
from .models import Asset,Server,SecurityDevice,StorageDevice,NetworkDevice
from .models import Software,IDC,Manufacturer,BusinessUnit,Contract
from .models import Tag,CPU,RAM,Disk,NIC,EventLog,NewAssetApprovalZone
from . import asset_handler

# Register your models here.
class NewAssetAdmin(admin.ModelAdmin):
    # 指定显示在Admin/NewAssetAdmin页面中的列栏名称，(修改页面上的字段)
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    # 设置list_filter属性后，可以激活修改列表页面的右侧边栏，用于对列表元素进行过滤
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    # 设置这个属性，可以为admin的修改列表页面添加一个搜索框
    search_fields = ('sn',)


    # Django的admin默认有一个delete操作的action，所有在admin中的模型都有这个action
    # 定义当前模型的新的其他 acitons 列表 ，使其有多种操作(执行)动作
    actions = ['approve_selected_new_assets']

    def approve_selected_new_assets(self, request, queryset):
        # 通过request.POST.getlist()方法 获得被打钩的checkbox对应的资产
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        success_upline_number = 0
        for asset_id in selected:
            # 对于每一个资产，创建一个asset_handler.ApproveAsset()的实例，
            # 然后调用实例的asset_upline()方法，并获取返回值。如果返回值为True，
            # 说明该资产被成功批准，那么success_upline_number变量+1，
            # 保存成功批准的资产数；
            obj = asset_handler.ApproveAsset(request, asset_id)
            ret = obj.asset_upline()
            if ret:
                success_upline_number += 1
        # 顶部绿色提示信息
        self.message_user(request, "成功批准  %s  条新资产上线！" % success_upline_number)
    # 用于在admin界面中为action提供中文显示。
    approve_selected_new_assets.short_description = "批准选择的新资产"

class AssetAdmin(admin.ModelAdmin):
    # 指定显示在Admin/NewAssetAdmin页面中的列栏名称，(修改页面上的字段)
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]


# 注册的时候，将原模型和AssetAdmin耦合起来
admin.site.register(Asset,AssetAdmin)
admin.site.register(Server)
admin.site.register(SecurityDevice)
admin.site.register(StorageDevice)
admin.site.register(NetworkDevice)

admin.site.register(Software)
admin.site.register(IDC)
admin.site.register(Manufacturer)
admin.site.register(BusinessUnit)
admin.site.register(Contract)

admin.site.register(Tag)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Disk)
admin.site.register(NIC)
admin.site.register(EventLog)
admin.site.register(NewAssetApprovalZone, NewAssetAdmin)
# 注册的时候，将原模型和NewAssetAdmin耦合起来