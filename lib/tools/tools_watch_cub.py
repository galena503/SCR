
import time,sys,os
import subprocess


class Tools_watch_sub():

    def check_sub_process(self, SCR, SCRfield):
        subs = SCR['sub_process']
        command = SCRfield['command']
        cmd_l = ['tasklist','/fo','csv']
        pid_set = set('')
        if command == 'bash':
            ps_str = subprocess.Popen(bash_l, shell=True, stdout=subprocess.PIPE)
        elif command == 'cmd':
            ps_str = subprocess.Popen(cmd_l, shell=True, stdout=subprocess.PIPE)
        for line in ps_str.stdout:
            hexline = str(line)
            pid = hexline.replace('\"','').split(',')[1]
            pid_set.add(pid)
            if pid == "PID":
                continue
            else:
                if int(pid) in subs:
                    SCR.state[pid] = 1
        SCR['sub_process'] = subs & pid_set
        return SCR





            

    def task_throw_sub(self, count):


st = 0
cmd = ['tasklist','/fo','csv']
subs = set('')
# winの場合
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
while True:
    
    if st == 0:

        st = 1
    time.sleep(1)




        #for sub_pid in subs:
        #    ps_line = line.split(',').replace('\"','')
        #    if str(sub_pid) == :
        #        print(str(sub_pid) + 'みつけたああああああああああああああああああ')
    #print(os.getpid())
    # log = popen_obj.returncode
    #print(log)
    #print(type(popen_obj.communicate()))
    #print(popen_obj.communicate())