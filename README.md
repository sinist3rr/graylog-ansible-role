graylog-ansible-role
=========
[![Build Status](https://travis-ci.org/sinist3rr/graylog-ansible-role.svg?branch=master)](https://travis-ci.org/sinist3rr/graylog-ansible-role)   

Installs Graylog on RedHat/CentOS servers.

Requirements
------------

Only CentOS version 7 is supported.

Role Variables
--------------

All variables can be viewed in the file `defaults/main.yml`.  
Nginx will be installed by default (`graylog_install_nginx`). 
The notification telegram plugin is enabled and will be installed by default (`graylog_install_telegram_alert`).    
Creating input via API is disabled by default (`graylog_create_input_api`).   

Dependencies
------------

None.

Example Playbook
----------------


    - hosts: servers
      roles:
         - { role: graylog-ansible-role }
           vars:
             graylog_root_timezone: "Europe/Kiev"
             graylog_elasticsearch_shards: 1


License
-------

GPL-3.0 

