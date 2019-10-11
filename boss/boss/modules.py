from datetime import datetime
from datetime import timedelta
class ProxyModules(object):
    def __init__(self,data):
        self.ip = data['ip']
        self.port = data['port']
        expire_dt = data['expire_time']
        expire_date = expire_dt.split(" ")[0]
        expire_time = expire_dt.split(" ")[1]
        year,month,day = expire_date.split('-')
        hour,minute,second = expire_time.split(':')
        self.expire_time = datetime(year=int(year),month=int(month),day=int(day),hour=int(hour),minute=int(minute),second=int(second))
        self.proxy="https://{}:{}".format(self.ip,self.port)
        print("%s---proxy",self.proxy)
        print("%s---expire_time",self.expire_time)
        self.blacked = False

    @property
    def is_expring(self):
        nowDt = datetime.now()
        print(self.expire_time-nowDt,"时间差")
        if (self.expire_time-nowDt) < timedelta(seconds=10):
            return True
        else:
            return False
