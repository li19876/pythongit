
import wmi


def get_cpu_info():
	c = wmi.WMI()
	#          print c.Win32_Processor().['ProcessorId']
	#          print c.Win32_DiskDrive()
	for cpu in c.Win32_Processor():
		return cpu.ProcessorId.strip()


print(get_cpu_info())
