import genshinstats as gs
import os
import time

gs.set_cookie(ltuid = int(os.environ.get('LTUID')), ltoken = os.environ.get('LTOKEN'))


now = time.localtime()
print ("%d/%d/%d %d:%d:%d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))




info = gs.get_daily_reward_info()
print('total rewards claimed:',info['total_sign_day'])
print("Get Reward :", gs.sign_in()) # signed you in, returns a bool whether it succeeded
info = gs.get_daily_reward_info()
print('total rewards claimed:',info['total_sign_day']) # check-in completed if increased
print("_________________________________")
