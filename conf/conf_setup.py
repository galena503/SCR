
default_SCRfield = {
    "state": {
        "myid": 0,
        "fid": 0,
        "bid": 0,
        "ids": [],
        "interpreter": "cmd",
        "ssh": []
    },
    "meta": {
        "near_field": [],
        "near_field_path": []
    }
}


default_SCRenv = {
		"pulse_rate": 0.1,
		"restart_flag": False,
		"end_flag": False,
		"max_sub_process": 2,
        "cpu_count": 0
}

default_SCR = {
    "now": 0,
    "sub_process": set(''),
    "state": {
        "1234" : 9,
        "5678" : 1
    }
}

default_SCRtask = {
	"tid": 1000000
	"d": {
        "priority": 0,
        "pid": 0,
        "lang":"",
        "data_key":"",
        "data_path":"",
        "file_name":"",
    }
}

default_SCRschedule = {
    "min": 0,
    "days1": False,
    "immortal_id":0,
    "immortal_pri":0,
    "d": {
        "priority": 0,
        "pid": 0,
        "lang":"",
        "data_key":"",
        "data_path":"",
        "file_name":"",
    }
}

default_SCRreceive = {
    "min": 0,
    "days1": False,
	"d": {
        "priority": 0,
        "pid": 0,
        "lang":"",
        "data_key":"",
        "data_path":"",
        "file_name":"",
    }
}