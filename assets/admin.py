from django.contrib import admin
from .models import Asset,Server,SecurityDevice,StorageDevice,NetworkDevice
from .models import Software,IDC,Manufacturer,BusinessUnit,Contract
from .models import Tag,CPU,RAM,Disk,NIC,EventLog,NewAssetApprovalZone
from . import asset_handler

# Register your models here.
class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    search_fields = ('sn',)
    # 定义当前模型的新acitons列表
    actions = ['approve_selected_new_assets']

    def approve_selected_new_assets(self, request, queryset):
        # 通过request.POST.getlist()方法 获得被打钩的checkbox对应的资产
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        success_upline_number = 0
        for asset_id in selected:
            obj = asset_handler.ApproveAsset(request, asset_id)
            ret = obj.asset_upline()
            if ret:
                success_upline_number += 1
        # 顶部绿色提示信息
        self.message_user(request, "成功批准  %s  条新资产上线！" % success_upline_number)
    # 用于在admin界面中为action提供中文显示。
    approve_selected_new_assets.short_description = "批准选择的新资产"

class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]



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