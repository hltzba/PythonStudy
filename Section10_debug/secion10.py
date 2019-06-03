# encoding:utf=8
#! python3
# section10.py - processs exception demo.
import traceback,logging
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s \n %(message)s \n ---------------------')
logging.basicConfig(filename='section10.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s \n %(message)s \n ---------------------')
def throwex():
    raise Exception('模拟异常咯')

def catchex():
    try:
        throwex()
    except Exception as ex:
        print(str(ex))
        #print('StackTrace'.center(18,'-'))
        #print(traceback.format_exc())
        logging.debug('StackTrace'.center(18,'-'))
        logging.error(traceback.format_exc())

catchex()

