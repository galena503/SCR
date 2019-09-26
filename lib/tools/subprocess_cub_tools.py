
from lib.tools.tools_data import Tools_data
from lib.tools.tools import Tools
from conf.sub import sub

class Subprocess_sub_tools():

    # 優先度が高い順にマークなしの物を選ぶ
    def choose_task(self, SCRtasks):
        for task in SCRtasks:
            if task.priority == 3 and task.pid == 0: # 優先度高
                return task
            if task.priority == 2 and task.pid == 0:
                taskp2 = task
        if not taskp2.tid == 1000000:
            return taskp2 # 優先度中
        else:
            for task in SCRtasks:
                if task.pid == 0:
                    return task # 優先度低
            # マークの無いタスクが無かったらプロセスを終了する
            exit()

    def mark_check(self, SCRtasks, now_pid):
        for task in SCRtasks:
            if task.pid == now_pid:
                return task
        return { "tid": 1000000 }

    def exec_task(self, task):
        command = []
        comarg = conf.interpreter
        lang = task.details.lang
        command.append(lang)

        if not task.details.ability == "":
            command.append(task.ability + task.details.file_name + comarg[lang].extension)
        elif not task.details.f_ability == "":
            command.append(task.f_ability + task.details.file_name + comarg[lang].extension)

        if not task.details.data_key == "":
            command.append(comarg[lang].data_key)
            command.append(task.details.data_key)

        if not task.details.data_path == "":
            command.append(comarg[lang].data_path)
            command.append(task.details.data_path)
        
        print('run : ' + command)
        subprocess.run(command)






