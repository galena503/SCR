
from datetime import datetime

class Tools_log:

    # error('[1,9]', '[エラー番号]', '[場所]', 'エラー文')
    def error(self, lv, no, ty, logstr):
        log = Log()
        if lv == 9:
            log.log_add(ty=ty, logfull='Fatal error - ' + no + ' - ' + logstr)
            log.log_add(ty=ty, logfull='Safely shuts down SCRsystem')
            log.log_add(ty=ty, logfull='loging for manipulator/log/' + ty + '.log')
            exit()
        elif lv == 1:
            log.log_add(ty=ty, logfull='Error - ' + no + ' - ' + logstr)

    def exception(self, lv, no, ty):
        log = Log()
        if lv == 1:
            log.log_add(ty=ty, logfull='exception - ' + no + ' - ' + logstr)

    def log_add(self, ty, logfull):
        print(ty + ' : ' + logstr)
        now = datetime.now()
        f = open('manipulator/log/' + ty +'.log','a')
        f.write(ty + ' : [' + now.strftime('%Y-%m-%d %H:%M:%S') + '] ' + logstr + '\n')
        f.close()