get-dns
==========

A program to get windows DNS records


### How to use?
* First install the dependencies
```
sudo python install-modules.py
```

* Add the Following line to your crontab
```
sudo python get-dns.py > /etc/hosts
```

* If you want to print the records to stdout
```
sudo python get-dns.py
```

* Note! your DNS server must be open the dns zone transfer settings.

### The configuration file 
* `client_hosts`: This is a hosts format file that contains your client you want to added.
* `except_hosts`: if you want to except some records, you can define in it.
* if the same records in both `client_hosts` and `except_hosts`, the `client_hosts` will be apply.


### Author
jiasir (Taio Jia) <jiasir@icloud.com>