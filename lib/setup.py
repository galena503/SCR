from lib.tools.tools_data import Tools_data
from lib.tools.tools_log import Tools_log
from lib.tools.tools import Tools
import conf.conf_setup as confs
import conf.conf_redis as confr

class Setup:
    # chain create SETUP
    # 'chain [fid]'
    # journal only
    # 
    def field(self, arg_obj, place):
        tod = Tools_data()
        to = Tools()
        log = Log()
        # fieldジャーナルの存在をチェック
        if tod.search_data(self, 'field', place, 'bool'):
            # 存在する場合は再起動なのでこのまま起動して良い
            if arg_obj.chain:
                # fieldデータが存在する、かつ引数が渡されたという事は既にデプロイされた所にchain-createしている。
                # 同じフォルダにchain-createするのはプロセスの競合を起こす事があるので致命的なエラーとして処理する。
                log.error(9, 'sf-001', 'setup.field', 'Unintended argument(s) < ' + sarg + ' >')
            else:
                # 取得する
                SCRfieldstr = tod.search_data(self, 'field', place, 'str')
                return to.sometype_to_json(SCRfieldstr,'python')
        else:
            # 存在しない場合は新規作成かchain-create
            tempSCRfield = confs.default_SCRfield
            if arg_obj.chain: # chain-createは引数が渡される
                # chain createで作る(scrctl chain-create 経由の起動のみ)
                # 渡されているファイルを見て自分のfidを調べ新しくidを振る
                tempSCRfield.state.fid, tempSCRfield.state.envid = to.get_other_id()
            else:
                # bidとfidとenvidを新規に作る
                tempSCRfield.state.bid = 0
                tempSCRfield.state.fid = 1
                tempSCRfield.state.envid = 1
            # 書き込み
            if not tod.create_data(self, 'journal/scr_f.journal', str(tempSCRfield), place):
                # 作る事ができない
                log.error(9, 'sf-002', 'setup.field', 'Unintended argument(s) < ' + sarg + ' >')
            return tempSCRfield


    # 
    def env(self, SCRfield, place, raw):
        log = Log()
        tod = Tools_data()
        to = Tools()

        # rediskey、またはfilepathを作成
        key = to.str_trans_type(SCRfield=SCRfield, ty='e')
        # データが存在するかチェック
        if tod.search_data(key=key, place=place, answer='bool'):
            # 存在する場合取得
            tempSCRenv_str = tod.search_data(key=key, place=place, answer='str')
            if raw:
                return tempSCRenv_str
            tempSCRenv = to.sometype_to_json(sometype=tempSCRenv_str, what_l='python')
            # 終了フラグと再起動フラグを元に戻す
            tempSCRenv.s.end_flag = False
            tempSCRenv.s.restart_flag = False
            return tempSCRenv
        else:
            # 存在しない場合confsから取得する
            tempSCRenv = confs.default_SCRenv
        # 環境情報に変更や無理が無いかチェックする
        tempSCRenv.e.cpu_count = to.cpu_count()
        # max_sub_processの調整
        if tempSCRenv.s.max_sub_process + 1 > tempSCRenv.e.cpu_count:
            tempSCRenv.s.max_sub_process = tempSCRenv.e.cpu_count - 1
        return tempSCRenv

    # 念の為取得
    def tasks(self, SCRfield, place):
        td = Tools_data()

        # key、またはpathを作成
        key = to.str_trans_type(SCRfield=SCRfield, ty='e')
        # データが存在するかチェック
        if tod.search_data(key=key, place=place, answer='bool'):
            # 存在する場合取得
            tempSCRenv_str = tod.search_data(key=key, place=place, answer='str')
            tempSCRenv = to.sometype_to_json(sometype=tempSCRenv_str, what_l='python')
            return tempSCRenv
        else:
            # 存在しない場合作成
            tempSCRenv = []
            return tempSCRenv


    # 起動時のコマンド引数の処理
    # 引数に入る候補 'chain'
    def arg_to_obj(self, sarg):
        arg_obj = {"arg":False, "chain":False}
        get = ''
        sarg_set = set(sarg)
        if 'chain' in sarg_set:
            arg_obj.chain = True
        return arg_obj
        
    # pool作成、journalも同時に扱う
    # 動作確認できたらredisを使うが基本的にjournalからredisへのデータ移行は行わない
    # コードを書き換えないとredisをonにできないので再起動では読み込まない
    def place_search(self):
        try:
            pool = redis.ConnectionPool(host=confr.address, port=confr.port, db=confr.db, decode_responses=True)
            rp = redis.StrictRedis(connection_pool=pool)
            rp.keys()
        except:
            print('Boot to journal mode')
            return == 'journal'
        print('Boot to redis mode')
        return == pool
