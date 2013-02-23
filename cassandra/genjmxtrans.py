#!/usr/bin/python

import os
import sys
import json
import urllib

my_cass_cluster = ["mycass01","mycass02"]
cf_config_url ="cf-config.json"

graphite_host = "graphite.myorg.com"
graphite_port = "2003"

cass_jmx_port = "8080"

def get_cassandra_config(hosts):
    url = cf_config_url
    print "Getting cassandra keyspace/cf configuration from %s" % url
    cassandra_config = json.load(urllib.urlopen(url))
    return cassandra_config


def generate_cass(node_array):
    cassandra_config = get_cassandra_config(node_array)
    for host in node_array:
        generate_host(host, "cassandra", cassandra_config)

def generate_host(host, type, cassandra_config):
    print "generating template for %(type)s: %(host)s" % { 'host': host, 'type': type }
    cass_template = open('templates/cassandra.template', 'r').read()
    cass_cache_template = open('templates/cassandra.cache.template', 'r').read()
    cass_cf_template = open('templates/cassandra.columnfamily.template', 'r').read()
    output_file = open("output/%(host)s-%(type)s.json" % { 'host': host, 'type': type }, 'w')

    caches = ""
    column_families = ""
    for keyspace in cassandra_config:
        for column_family in keyspace['columnFamilies']:
            print "creating configuration for keyspace: %s and column family: %s" % (keyspace['name'], column_family['name'])
            column_families = column_families +  (cass_cf_template % { "keyspace": keyspace['name'], "column_family": column_family['name'],  "graphite_host": graphite_host, "graphite_port": graphite_port })
            caches = caches + (cass_cache_template % { "keyspace": keyspace['name'], "column_family": column_family['name'],  "graphite_host": graphite_host, "graphite_port": graphite_port })
    contents = cass_template % { 'host' : host, "port": cass_jmx_port, "caches": caches, "column_families": column_families ,  "graphite_host": graphite_host, "graphite_port": graphite_port }
    output_file.write(contents)
    output_file.close()


generate_cass(my_cass_cluster)


