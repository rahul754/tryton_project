from django.conf import settings
import sys, os
import warnings
warnings.filterwarnings("ignore",message="ols style callback,usecb_fun(ok,store)instead ")

TRYTOND_PATH = settings.TRYTOND_PATH

DIR =os.path.abspath(os.path.normpath(os.path.join(TRYTOND_PATH,'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0,os.path.dirname(DIR))


from trytond.modules import register_classes
from tryton.pool import Pool
from trytond.backend import Database
from trytond.tools import Cache

#register class populates the pool of moduls:

register_classes()


#Instantiate the dataase and the pool
DB = Database(settings,TRYTON_db).connect()
POOL = Pool(setting.TRYTON_DB)
POOL.init()
user_obj  = POOL.get('res_user')
cursur = DB.cursor()
Cache.clean(settings.TRYTON_DB)
try:
    #user 0 is  aroot user .we ue it to get user id
    USER = user.obj.search(cursor,0, [
            ('login','=',settings.TRYTON_UN),
            ], limit=1)[0]
finally:
    cursor.close()
    Cache.reset(settings.TRYTON_DB) 



























 
