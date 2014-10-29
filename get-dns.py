#!/usr/bin/env python
__author__ = 'Taio'

import os
import os.path
import dns.query
import dns.zone
import logging
from utils.noflib import Noflib

run = Noflib()

logger = logging.getLogger('get-dns')
logging.basicConfig(filename='/var/log/get-dns/get-dns.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dcAdd = '172.20.10.75'
domainName = 'spidc1.com'
z = dns.zone.from_xfr(dns.query.xfr(dcAdd, domainName))
names = z.nodes.keys()
names.sort()


def print_local_host():
    print '127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4'
    print '::1         localhost localhost.localdomain localhost6 localhost6.localdomain6'


def print_records_stdout():
    """Print records only to stdout"""
    for i in names:
        line = z[i].to_text(i).split()
        logger.info(line[3])
        if line[3] == 'A':
            logger.info(line[4])
            new_line = line[4] + ' ' + line[0] + '.spidc1.com'
            if new_line not in get_hosts():
                logger.info(new_line)
                print new_line


def gen_records_spidc1():
    """Write to /etc/hosts file"""
    try:
        with open('/etc/hosts', 'a') as f:
            for i in names:
                f.write(z[i].to_text(i))
    except IOError:
        logger.error(IOError.__doc__)
        print IOError.__doc__


def get_hosts():
    """
    Get Linux hosts file.
    :return string:
    """
    with open('/etc/hosts', 'r') as h:
        return h.read()


def main():
    if not os.path.exists('/var/log/get-dns'):
        run.execute_get_output('sudo', 'mkdir', '/var/log/get-dns')

    print_local_host()
    print_records_stdout()


if __name__ == '__main__':
    if os.getuid() == 0:
        main()
    else:
        print 'You do not have permission, please run as root.'
        exit()