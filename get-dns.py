__author__ = 'Taio'


import os.path
import dns.query
import dns.zone
import logging
from utils.noflib import Noflib

run = Noflib()

logger = logging.getLogger('get-dns')
logging.basicConfig(filename='get-dns.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dcAdd = '172.20.10.75'
domainName = 'spidc1.com'
z = dns.zone.from_xfr(dns.query.xfr(dcAdd, domainName))
names = z.nodes.keys()
names.sort()

def print_records_stdout():
    '''Print records only to stdout'''
    for i in names:
        if i.find('IN A'):
            print z[i].to_text(n)

def gen_records_spidc1():
    '''Write to /etc/hosts file'''
    try:
        with open('/etc/hosts', 'a') as f:
            for i in names:
                f.write(z[i].to_text(n))
    except IOError:
        print IOError.__doc__

def main():
    if not os.path.exists('/var/log/get-dns'):
        run.execute_get_output('sudo', 'mkdir', '/var/log/get-dns')

    print_records_stdout()
    #gen_records_spidc1()

if __name__ == '__main__':
    if os.getuid() == 0:
        main()
    else:
        print 'You do not have permission, please run as root.'
        exit()