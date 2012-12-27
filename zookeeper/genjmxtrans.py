#!/usr/bin/python

import os
import sys


prod_zk_cluster = ["zk01.myorg.com", "zk02.myorg.com", "zk03.myorg.com"]

zk_template = open('templates/zookeeper.template', 'r').read()

zk_jmx_port="9011"

graphite_host = "graphite.myorg.com"
graphite_port = "2003"
output_dir="output"


def generate_zk(node_array):
    for host in node_array:
        generate_host(host, "zookeeper", zk_template)

def generate_host(host, type, template):
    print "generating template for %(type)s: %(host)s" % { 'host': host, 'type': type }
    output_file = open("%(output_dir)s/%(host)s-%(type)s.json" % { "output_dir": output_dir, "host": host, "type": type }, "w")
    output_file.write(template % { "port" : zk_jmx_port , "host" : host, "graphite_host": graphite_host, "graphite_port": graphite_port  })
    output_file.close()

generate_zk(prod_zk_cluster)



