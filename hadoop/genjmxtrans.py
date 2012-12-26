#!/usr/bin/python

import os
import sys


ny_hadoop_nodes = ["hadoop01.myorg.com", "hadoop02.myorg.com"]
ny_hadoop_namenode = "namenode01.myorg.com"
ny_hadoop_jobtracker = "jobtracker01.myorg.com"

tt_template = open("templates/tasktracker.template", "r").read()
dn_template = open("templates/datanode.template", "r").read()
nn_template = open("templates/namenode.template", "r").read()
jt_template = open("templates/jobtracker.template", "r").read()

dn_port = "9013"
tt_port = "9015"
nn_port = "9011"
jt_port = "9014"

graphite_host = "graphite.myorg.com"
graphite_port = "2003"
output_dir="output"

def generate_cluster(node_array):
    for host in node_array:
        generate_host(host, "datanode", dn_template, dn_port)
        generate_host(host, "tasktracker", tt_template, tt_port)

def generate_nn(host):
    generate_host(host, "namenode", nn_template, nn_port)

def generate_jt(host):
    generate_host(host, "jobtracker", jt_template, jt_port)

def generate_host(host, type, template, port):
    print "generating template for %(type)s: %(host)s" % { "host": host, "type": type }
    output_file = open("%(output_dir)s/%(host)s-%(type)s.json" % { "output_dir": output_dir, "host": host, "type": type }, "w")
    output_file.write(template % { "port" : port , "host" : host, "graphite_host": graphite_host, "graphite_port": graphite_port  })
    output_file.close()

generate_nn(ny_hadoop_namenode)
generate_jt(ny_hadoop_jobtracker)
generate_cluster(ny_hadoop_nodes)



