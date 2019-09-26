from lib.tools.tools import Tools
from lib.tools.tools_data import Tools_data
from lib.tools.tools_log import Tools_log
import conf.conf_setup as confs

class Second:
    # オンタイムタスクリストを取得して必要があればタスクに追加
    # SCRtasksに追加できるのはここのみ
    # 1 情報取得
    # 2 SCRscheduleからSCRtasksに追加
    # 3 SCRreceiveからSCRtasksに追加
    # 4 SCRreceiveからSCRscheduleに追加
    def task_check(self, SCR, SCRfield, SCRtasks, place):
        log = Tools_log()
        td = Tools_data()
        to = Tools()

        tempSCR = SCR
        tempSCRtasks = SCRtasks
        addSCRtasks = []

        # SCRscheduleを取得
        keyss = to.str_trans_type(SCRfield=SCRfield, ty='sc')
        SCRspm_list = tod.search_data(key=keyss, place=place, 'list')

        # SCRreceiveを取得
        keysr = to.str_trans_type(SCRfield=SCRfield, ty='re')
        SCRreceive = tod.search_data(key=keysr, place=place, 'list')
        # SCRreceiveを消去
        truncate_data(key=keysr, place=place)

        # SCRscheduleからSCRtasksに追加
        for ss in SCRschedule:
            if ss.days1 and ss.min == SCR.n:
                ast = confs.default_SCRtask
                ast.d = ss.d
                ast.tid = tempSCR.mtid + 1
            if SCR.n % ss.min == 0:
                ast = confs.default_SCRtask
                ast.d = ss.d
                ast.tid = tempSCR.mtid + 1
        
        # SCRreceiveからSCRtasksに追加



        # SCRreceiveからSCRscheduleに追加






        # SCRscheduleとSCRreceiveから必要なデータをSCRtasksに追加

        # 書き込み
        SCRtasks.append(addSCRtasks)















        ###### 書き直し中
        SCRreceive_str = td.get_str(sid=SCRfield.state.myid, sfid=SCRfield.state.fid, ty='re', action='pop')
        if SCRreceive_str == 'nofile': # redis切り替え直後
            return SCR, tempSCRtasks
        else:
            SCRreceive = to.sometype_to_json(SCRschedule_str)

        # スケジュールデータを取得
        SCRschedule_str = get_datastr(sid=SCRfield.state.myid, sfid=SCRfield.state.fid, ty='sc', action='get')
        if SCRschedule_str == 'nofile': # redis切り替え直後
            return SCR, tempSCRtasks
        else:
            if not str(tempSCRschedule) == SCRschedule_str:
                tempSCRschedule = to.sometype_to_json(SCRschedule_str)

            # scheduleの更新
            for re in SCRreceive:
                if re.min == 0:
                    # 普通のタスク
                    tempSCRtasks.append({"tid":SCR.lt,"d":re.d})
                    SCR.lt = SCR.lt + 1
                else:
                    temp_schedule = confs.default_SCRschedule
                    temp_schedule["min"] = re.min
                    temp_schedule["days1"] = re.days1
                    tempSCRschedule.append(temp_schedule)



            # scheduleの書き込み

            

            # ユーザーコードフォルダデータを更新しておく
            # SCRcordsはflaskからの読み取り用
            SCRcords = to.glob_codes()
            td.insert_jou(sfid=SCRfield.state.myid, sfid=SCRfield.state.fid, ty='co', ob=SCRcords)

            # schedule_taskを見て必要であればタスクセット
            if not len(tempSCRschedule) == 0:
                for schedule in tempSCRschedule:
                    if schedule.days1:
                        if SCR.n / schedule.min == 1:
                            # タスクセット
                            tempSCRtasks.append({"tid":SCR.lt + 1, "d":schedule.d})
                        if schedule.min % SCR.n == 0 and schedule.days1:
                            # タスクセット
                            tempSCRtasks.append({"tid":SCR.lt + 1, "d":schedule.d})
        
        return SCR,tempSCRtasks

    


                



       
