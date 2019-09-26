from lib.tools.tools_task import Tools_task
from lib.tools.tools_data import Tools_data
from lib.tools.tools_watch_sub import Tools_watch_sub
from lib.tools.tools import Tools
from lib.tools.tools_time import Tools_time
from lib.tools.tools_log import Tools_log

class Rotation:

    # タスクの状況管理とサブプロセスの立ち上げ
    def task_throw(self, SCR, SCRfield, SCRenv, SCRtasks, place):

        # まずsleep
        tot = Tools_time()
        tot.sleep(SCRenv.pulse_rate)

        # 現在の秒取得
        tempSCR = SCR
        tempSCR['n'] = tot.now_sec()

        # プロセスの状態チェック開始
        towc = Tools_watch_sub()
        
        ccpSCR = towc.check_sub_process(SCR=tempSCR, SCRfield=SCRfield)
        tempSCR['sub_process'] = ccpSCR.sub_process

        # プロセスがmax使用なら中断
        mcp = SCR.state.max_sub_process
        rest_sub = towc.can_throw_task(tempSCR, mcp)
        if 0 == rest_sub:
            return tempSCR, SCRtasks
        else:
            # taskがあるかチェック
            if len(SCRtasks) == 0:
                # 無ければmaxtidを1に戻して終了
                tempSCR.mtid = 1
                return tempSCR, SCRtasks

            # SCRspm_listは重複する物なので毎回チェックしなければいけない
            # => to.check_duplicate_tid()

            to = Tools()
            # ファイル名の末尾にはtidを100で割った数字が付く
            num = str(tempSCR.mtid)[:-2]
            # 書き換える為のSCRtasks
            renewSCRtasks = SCRtasks
            # 新しく承認するセット
            addSCRspa = set()
            # 終了済みセット
            
            # maxtid[:-2]が2以上の時、以前のデータもチェックしなければいけない
            # keyのnum部分の違うset同士を混ぜる事はできない
            if not num == '1':
                num_ob = str(int(num) - 1)
                # まずは存在チェック
                keyspm_ob = to.str_trans_type(SCRfield=SCRfield, ty='spm', num=num_ob)
                if tod.search_data(key=keyspm_ob, place=place, 'bool'):
                    # 存在しているという事は終わっていない可能性がある。
                    # 未実装：サブプロセスが異常終了をした場合、データの差分が出る場合があるが、
                    # SCRは異常終了したものをもう一度流してしまう。
                    keyspa_ob = to.str_trans_type(SCRfield=SCRfield, ty='spa', num=num_ob)
                    keyspe_ob = to.str_trans_type(SCRfield=SCRfield, ty='spe', num=num_ob)

                    SCRspm_ob_list = tod.search_data(key=keyspm_ob, place=place, 'list')
                    SCRspm_ob_set = set(to.check_duplicate_tid(pt_list=SCRspm_ob_list))
                    SCRspa_ob_set = set(tod.search_data(key=keyspa_ob, place=place, 'list'))
                    SCRspe_ob_set = set(tod.search_data(key=keyspe_ob, place=place, 'list'))
                    if SCRspm_ob_set == SCRspa_ob_set and SCRspm_ob_set == SCRspe_ob_set:
                        # すべて完了しているタスクしか入っていない為、消去してよい
                        tod.truncate_data(key=keyspm_ob, place=place)
                        tod.truncate_data(key=keyspa_ob, place=place)
                        tod.truncate_data(key=keyspe_ob, place=place)
                    elif not SCRspm_ob_set == SCRspa_ob_set:
                        # 承認待ちタスクがまだ残っている場合は承認してtaskにpidを追加しなければならない
                        addSCRspa.add( SCRspm_ob_set - SCRspa_ob_set )
                        # 承認する事をSCRspa_setに書き込み、サブプロセスに伝える
                        add_spa_str = addSCRspa.join('\n')
                        tod.insert_data(key=keyspa_ob, ob_set=add_spa_str, place=place)
                    
            # まずは存在チェック
            keyspm = to.str_trans_type(SCRfield=SCRfield, ty='spm', num=num)
            if tod.search_data(key=keyspm, place=place, 'bool'):
                # 存在しているという事は終わっていない可能性がある。
                # 未実装：サブプロセスが異常終了をした場合、データの差分が出る場合があるが、
                # SCRは異常終了したものをもう一度流してしまうのでユーザーデータが重複する可能性がある
                keyspa = to.str_trans_type(SCRfield=SCRfield, ty='spa', num=num)
                keyspe = to.str_trans_type(SCRfield=SCRfield, ty='spe', num=num)

                SCRspm_list = tod.search_data(key=keyspm, place=place, 'list')
                SCRspm_set = set(to.check_duplicate_tid(pt_list=SCRspm_list))
                SCRspa_set = set(tod.search_data(key=keyspa, place=place, 'list'))
                SCRspe_set = set(tod.search_data(key=keyspe, place=place, 'list'))
                if SCRspm_set == SCRspa_set and SCRspm_set == SCRspe_set:
                    # すべて完了しているタスクしか入っていない為、消去してよい
                    tod.truncate_data(key=keyspm, place=place)
                    tod.truncate_data(key=keyspa, place=place)
                    tod.truncate_data(key=keyspe, place=place)
                elif not SCRspm_set == SCRspa_set:
                    # 承認待ちタスクがまだ残っている場合は承認してtaskにpidを追加しなければならない
                    temp_addssst = SCRspm_set - SCRspa_set
                    # 承認する事をSCRspa_setに書き込み、サブプロセスに伝える
                    add_spa_str = temp_addssst.join('\n')
                    tod.insert_data(key=keyspa_ob, ob_set=add_spa_str, place=place)
                    addSCRspa.add(temp_addssst)

            # taskidの最大数を調べる為の変数
            task_ids = []
            # タスクが終了したのでSCRtasksから削除すべきindexを表す変数
            pop_index = []

            # addSCRtask  ('1-2','2-3','4-1')
            addSCRspa_l = list(addSCRspa)

            # SCRspaに追加したタスクの承認情報をSCRtasksに反映させる
            # 同時にtaskidをすべてtask_idsに取得する
            for tli in renge(len(SCRtasks)):
                task_ids.add(SCRtasks[tli].tid)
                if SCRtasks[tli].pid == 0:
                    for addSCRspa in addSCRspa_l
                        ass = addSCRspa.split('_')
                        if SCRtasks[tli].tid == ass[1]:
                            SCRtasks[tli]d.pid = ass[0]

            # 取得したsetから最大taskidをSCRに渡す
            # 未実装：必要か考える
            maxid = max(task_ids)
            tempSCR.mtid = maxid

            # タスク承認が終わったので必要な分サブプロセスを立ち上げる
            
            # 必要なプロセス数を取得
            want_process_count = len(addSCRspa)

            # 立ち上げ可能な数を調べる
            if rest_sub > want_process_count:
                towc.task_throw_sub(count=want_process_count)
            else:
                towc.task_throw_sub(count=rest_sub)
            

        # SCRtasksに反映
        keyst = str_trans_type(SCRfield=SCRfield, ty='t')
        # 消去
        ttd = tod.truncate_data(key=keyst, place=place)
        # 書き込み
        tcd = tod.create_data(key=keyst, ob_str=str(tempSCRtasks), place=place)

        if ttd and tcd:
            return tempSCR, tempSCRtasks

        








        

