volhit.redis
============

This installs the Redis and Redis Tools

Requirements
------------

No

Role Variables
--------------

- redis_host is the name of redis host )
- redis_port is the port
- redis_database is the count of db in the redis
- redis_timeout (in seconds) is connection timeout
- redis_keepalive (in seconds) is redis tcp-keepalive

Dependencies
------------

No

Example Playbook
----------------

    - hosts: redis
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPLv3
