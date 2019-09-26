
import subprocess
import time,sys,os
from lib.tools.tools_task import Tools_task
from lib.tools.subprocess_sub_tools import Subprocess_sub_tools
from lib.tools.tools_redis import Tools_redis
from lib.tools.tools_journal import Tools_journal
from lib.tools.tools import Tools
from lib.tools.sp_sub_tools import Sp_sub_tools
from lib.tools.setup import Setup


    def main():
        # タスクチェック開始
        to = Tools()
        tot = Tools_task()
        tod = Tools_data()
        tor = Tools_redis()
        scto = Subprocess_sub_tools()

        marktask = ''
        SCRfield = setup.field()
        now_pid = os.getpid()
        task = { "tid":1000000 }
        while True:

# numを判定しなければいけない

            # データをマークした時点でそのタスクはmarkしたpidのサブプロセスしか処理できない為、
            # markしたら必ずそのプロセスで処理をする
            # 名前を付けて呼び出す事でもしかしたら回避できる？
            if marktask == '':
                # タスクがあるかのチェックをして無ければ終了
                if SCRfield.mode.status_set == 'journal':
                    SCRtasks_str = toj.get_jou(sid=SCRfield.state.myid, sfid=SCRfield.state.fid, ty='t')
                elif SCRfield.mode.status_set == 'redis':
                    SCRtasks_str = tor.get_redis(sid=SCRfield.state.myid, sfid=SCRfield.state.fid, ty='t')
                if SCRtasks_str == 'nofile':
                    exit() # 今までにタスクが一回も投げられていないかredis切り替え直後
                else:
                    SCRtasks = to.jl_fall(SCRtasks_str,'python')
                    # タスクデータが無ければ承認待ちアイドリング
                    if len(SCRtasks) == 0:
                        exit()
                    # 本体プロセスから承認が下りているタスクデータがあるかチェック


                    # 実行できるものが無ければ{ "tid": 1000000 }が返る
                    task = scto.mark_check(SCRtasks=SCRtasks,now_pid=now_pid)
                    
                    if task.tid == 1000000: # タスクデータあり　かつ　未選択
                        # タスクデータを選ぶ
                        task = scto.choose_task(SCRtasks)
                        # タスクデータをマークして承認を仰ぐ

                        # この時点で落ちる事は許されない仕様になってしまう。
                        # 名前を付けて呼び出す事でもしかしたら回避できる？
                        if SCRfield.mode.status_set == 'journal':
                            marktask = tod.insert_jou(task.tid, now_pid, 'c',num=num)
                        elif SCRfield.mode.status_set == 'redis':
                            marktask = tor.mark_task_redis(task.tid, now_pid, 'c')
                    else: # タスクデータがある　
                        scto.exec_task(task=task,inte=SCRfield.state.interpreter)
                        # 終了
                        if SCRfield.mode.status_set == 'journal':
                            marktask = toj.mark_task_jor(task.tid, task_pid, 'f')
                        elif SCRfield.mode.status_set == 'redis':
                            marktask = tor.mark_task_redis(task.tid, task_pid, 'f')
                        marktask = ''
                    


if __name__ == '__main__':
    main()










time.sleep(0.1)
for i in range(50):
    time.sleep(0.1)
    print('test' + str(i))
sys.exit(1) # 正常終了