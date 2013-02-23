Introduction
============
Python scripts for generating [JMXTrans](https://github.com/lookfirst/jmxtrans) JSON configuration files for Apache Hadoop, Apache Zookeeper and Apache Cassandra.

I use these when I add a new node to these clusters or a new column family to Cassandra. I update the script with the new node, run these python scripts and update the JMXTrans server JSON files.

These were tested with the following versions:

* Apache Hadoop: 0.20.2
* Apache Zookeeper: 3.3.4
* Apache Cassandra: 1.09

Installation
============
There is no installation look at the various ```genjmxtrans.py``` and specify the host names for each cluster.
