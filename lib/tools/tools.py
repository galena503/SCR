import json,random,multiprocessing

class Tools:

    # タイプの判明していない変数をjsonに変換する
    def sometype_to_json(self, sometype, what_l):
        re = Tools()
        if type(sometype) is dict:
            for jk in list(sometype.keys()):
                sometype[jk] = re.sometype_to_json(sometype=sometype[jk],what_l=what_l)
            return sometype
        elif type(sometype) is list:
            for j_stt in range(len(sometype)):
                sometype[j_stt] = re.sometype_to_json(sometype=sometype[j_stt],what_l=what_l)
            return sometype
        elif type(sometype) is str or type(sometype) is int or type(sometype) is bool:
            try:
                res_json = json.loads(sometype)
                return re.sometype_to_json(sometype=res_json,what_l=what_l)
            except json.JSONDecodeError as e:
                if sometype == 'True':
                    if what_l == 'python':
                        return True
                elif sometype == 'False':
                    if what_l == 'python':
                        return False
                return sometype 
            except Exception as e:
                return sometype

    # コアの数を調べる
    def cpu_count(self):
        return multiprocessing.cpu_count()


    # codesフォルダの中を調べる
    # return <json>
    def glob_codes(self):
        SCRcords = []
        path_list_1 = glob.glob('codes/*')
        for path_1 in path_list_1:
            folder_name = path_1[6:]
            if folder_name == 'ignore':
                continue
            file_list = []
            path_list_2 = glob.glob('codes/' + folder_name + '/*')
            for path_2 in path_list_2:
                file_name = path_2[7+len(folder_name):]
                file_list.append(file_name)
            SCRcords.append( { "folder_name":folder_name, "file_list":file_list } )
        return SCRcords

    # クエリをpath、またはkeyに変換する
    # SCRfieldには対応できない
    # return <str>
    def str_trans_type(self, SCRfield, ty, num):
        sid = SCRfield.state.myid
        sfid = SCRfield.state.fid
        if ty == 'sp':
            trans_str = 'scr_sp_' + num
        else:
            trans_str = 'scr_' + sfid + '_' + sid + '_' + ty

        if SCRfield.mode.status_set == journal:
            trans_str = trans_str
        return trans_str

    # fieldファイルを探してfidとenvidを取得
    # return int,int
    def get_other_id():
        # chain-createでの起動でしか呼ばれないのでredisは非対応のままで良い
        path_list = glob.glob('journal/*')
        envid_list = []
        fid = 0
        for path in path_list:
            if path in '_e'
                p_list = path.split('_')
                fid = int(p_list[1])
                envid_list.append(int(p_list[2]))
        new_envid = max(set(envid_list)) + 1
        return fid, new_envid

    # リストの中にtidの被っているものが無いか調査してlistを返す
    def check_duplicate_tid(self, pt_list):
        unique_set = set()
        pop_list = []
        for pt_index in range(len(pt_list)):
            ltp = pt_list[pt_index].split('_')
            if ltp[1] in unique_set:
                pop_list.append(pt_index)
            unique_set.add(ltp)
        for pop_in in reversed(pop_list):
            pt_list.pop(pop_in)
        return pt_list
            