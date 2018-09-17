import platform
import win32com
import wmi

class Win32Info(object):

    def __init__(self):
        # 固定用法，更多内容请参考模块说明
        self.wmi_obj = wmi.WMI()
        self.wmi_service_obj = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        self.wmi_service_connector = self.wmi_service_obj.ConnectServer(".", "root\cimv2")

    '''
        def get_cpu_info(self):
            """
            获取CPU的相关数据，这里只采集了三个数据，实际有更多，请自行选择需要的数据
            :return:
            """
            data = {}
            cpu_lists = self.wmi_obj.Win32_Processor()
            # cpus 对象  服务器可以多个cpu,每个CPU又可以多核
            for cpu in range(len(cpu_lists)):
                print(cpu_lists[cpu])
            # print(cpu_lists)  __str__
            #[<_wmi_object: b'\\\\LINUIX\\root\\cimv2:Win32_Processor.DeviceID="CPU0"'>]
            # print(cpu.NumberOfCores) 注意此处得遍历打印
            cpu_core_count = 0
            for cpu in cpu_lists:
                print(cpu.NumberOfCores)  # 我的1个cpu 2个核
                cpu_core_count += cpu.NumberOfCores
    
            #print(cpu_lists[0])
            cpu_model = cpu_lists[0].Name   # CPU型号（所有的CPU型号都是一样的）
            data["cpu_count"] = len(cpu_lists)      # CPU个数
            data["cpu_model"] = cpu_model
            data["cpu_core_count"] = cpu_core_count  # CPU总的核数
    
            #return data
            print(data)
    a = Win32Info()
    a.get_cpu_info()
    '''

    def get_disk_info(self):
        """
        硬盘信息
        :return:
        """
        data = []


        obj = self.wmi_obj.Win32_DiskDrive()
        print(obj)
        # [<_wmi_object: b'\\\\LINUIX\\root\\cimv2:Win32_DiskDrive.DeviceID=
        # "\\\\\\\\.\\\\PHYSICALDRIVE0"'>]
        # print(type(obj))  # 列表  <class 'list'>
        # __str__
        print(obj[0])  # 打印出来同下
        for i in range(len(obj)):
            print(obj[i])



        # for disk in self.wmi_obj.Win32_DiskDrive():  # 每块硬盘都要获取相应信息
        #     item_data = dict()
        #     iface_choices = ["SAS", "SCSI", "SATA", "SSD"]
        #     for iface in iface_choices:
        #         if iface in disk.Model:
        #             item_data['iface_type'] = iface
        #             break
        #     else:
        #         item_data['iface_type'] = 'unknown'
        #     item_data['slot'] = disk.Index
        #     item_data['sn'] = disk.SerialNumber
        #     item_data['model'] = disk.Model
        #     item_data['manufacturer'] = disk.Manufacturer
        #     item_data['capacity'] = int(int(disk.Size) / (1024 ** 3))
        #     data.append(item_data)
        #
        # return {'physical_disk_driver': data}
a = Win32Info()
a.get_disk_info()