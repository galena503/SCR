# coding: UTF-8

# souruvei code 

import sys
from lib.setup import Setup
from lib.rotation import Rotation
from lib.second import Second

def scr():
    u = Setup()
    r = Rotation()
    s = Second()
    arg_obj = su.arg_to_obj(sys.argv)
    SCR = { "n":0 ,"sub_process":[], "mtid": 0}
    place = su.place_search()
    print('>>> SCR start >>>')
    while True:
        # setup
        SCRfield = su.field(place=place, arg_obj=arg_obj)
        SCRenv = su.env(SCRfield=SCRfield, raw=False)
        if SCRenv.end_flag:
            exit()
        SCRenv_raw = str(SCRenv)
        SCRtasks = su.tasks(SCR=SCR, SCRfield=SCRfield, place=place)
        while True:
            # Rotation
            nowsec = SCR.n
            SCR, SCRtasks = r.task_throw(SCR=SCR, SCRfield=SCRfield, SCRenv=SCRenv, SCRtasks=SCRtasks, place=place)
            if SCR.n != nowsec:
                # Second
                SCR.n = nowsec
                SCR, SCRtasks = s.task_check(SCR=SCR, SCRtasks=SCRtasks, place=place)
            if not SCRenv_raw == su.env(SCRfield=SCRfield, raw=True):
                break
        print('>>> SCR restart >>>')

if __name__ == "__main__":
    scr()