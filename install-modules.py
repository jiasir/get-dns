__author__ = 'Taio'


from utils.noflib import Noflib
import logging

logger = logging.getLogger('install-modules')
logging.basicConfig(filename='install-modules.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


run = Noflib()



def get_modules():
    '''get modules from github'''
    run.execute_get_output('git', 'clone', 'https://github.com/rthalley/dnspython.git')

def install_modules():
    '''install dnspython to package-sites'''
    run.execute_get_output('python', 'setup.py', 'install')

