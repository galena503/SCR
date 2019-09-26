
from manipulator.tools import Tools
import redis

class Flask_controller:


    def timer_change(self,json):
        tls = Tools()
        cr = redis.StrictRedis(host='192.168.99.100', port=6379, db=0)
        tojsde_json = str(json)
        cr.set('cr_task_0',tojsde_json)

