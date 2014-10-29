__author__ = 'Taio'

import os
from utils.noflib import Noflib
import logging

logger = logging.getLogger('install-modules')
logging.basicConfig(filename='/var/log/get-dns/install-modules.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


run = Noflib()




def get_modules():
    '''get modules from github'''
    run.execute_get_output('git', 'clone', 'https://github.com/rthalley/dnspython.git')

def install_modules():
    '''install dnspython to package-sites'''
    run.execute_get_output('python', 'dnspython/setup.py', 'install')


def main():
    if not os.path.exists('/var/log/get-dns'):
        logger.info('Making directory /var/log/get-dns')
        run.execute_get_output('sudo', 'mkdir', '/var/log/get-dns')

    logger.info('Getting modules')
    get_modules()
    logger.info('Installing modules')
    install_modules()



if __name__ == '__main__':
    if os.getuid() == 0:
        main()
    else:
        print 'You do not have permission, please run as root.'
        exit()