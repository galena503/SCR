import os
import glob
import time

# redisの用意と設定が済んでいる場合はコメントアウトをはずす
# 
import redis
import conf.redis as confr


# redisは必ず取得する際のデータ型をそのまま文字列にした状態で書き込む
class Tools_data:


    # keyはファイルパス、またはrediskeyのどちらかが渡される
    # placeのtypeは
    #   redis.connection.ConnectionPool
    #   str
    # のどちらか

    # 指定されたファイルの末尾に追加する
    # return <bool>
    def insert_data(self, key, ob_set, place):
        try:
            if type(place) == redis.connection.ConnectionPool:
                rp = redis.StrictRedis(connection_pool=place)

        except:
            print('redis error')
            # 致命的なエラーとして処理する
            # タスクデータが失われる為journalに切り替えてはいけない

        if place == 'journal':
            try:
                f = open(path, "a")
                wd = list(ob_set)
                f.write(wd.join('\n'))
                f.close()
            except:
                return False
            return True

    # 指定されたデータを作成する
    # return <bool>
    def create_data(self, key, ob_str, place):
        if place == 'redis':

        elif place == 'journal':
            try:
                f = open(key, "w")
                f.write(ob_str)
                f.close()
            except:
                return False
            return True
    
    # 指定されたデータを消去する
    # return <bool>
    def truncate_data(self, key, place):
        if place == 'redis':

        elif place == 'journal':
            try:
                os.remove(key)
            except:
                return False
            return True

    # SCRfieldデータを探して取得する
    # return <jsonstr>
    def search_data(self, key, place, answer):
        # fieldデータはテキストファイル限定
        # keyを渡せないので自身のフォルダにある物を見つけなければいけない
        if key == 'field':
            jour_list = glob.glob('journal/*')
            for jour_path in jour_list:
                if '_f' in jour_path:
                    if answer == 'bool':
                        return True
                    elif answer == 'str':
                        key = jour_path
            if key == 'field':
                return False
        # fieldデータ以外
        if place == 'redis':

        elif place == 'journal':
            data_set = set(glob.glob(key))
            if len(data_list) == 0:
                return 'False'
            if data_set in filename:
                f = open(key)
                temp_str = ''.join(f)
                f.close()
                if answer == 'list':
                    return temp_str.split('\n')
                return temp_str
        


            


        
