#!/usr/bin/env python
import os

# output helper
def show(caption, body):
    print '-- ', caption, ': --->\n', body, '\n<---'

from linode import api as linode_api
api = linode_api.Api(os.environ['LINODE_API_KEY'])

linodes = api.linode_list()
formatted = "\n".join(["{0}: {1}".format(linode['LABEL'], linode['LINODEID']) for linode in linodes])
show('Known hodes', formatted)

distrs = sorted(api.avail_distributions(), key=lambda x: x['CREATE_DT'], reverse=True)
formatted = "\n".join(
        [ "'{0}' -> Distribution Id: {1}, MinImgSize: {2}, is64Bit: {3}".
            format(distr['LABEL'], distr['DISTRIBUTIONID'], distr['MINIMAGESIZE'], distr['IS64BIT'])
            for distr in distrs ])
show('Distributions available', formatted)

datacenters = api.avail_datacenters()
formatted = "\n".join(
        [ "'{0}' -> Id: {1}, Abbr: {2}".
            format(dc['LOCATION'], dc['DATACENTERID'], dc['ABBR'])
            for dc in datacenters])
show('Datacenters', formatted)

plans = api.avail_linodeplans()
formatted = "\n".join(["{0}: {1}".format(plan['LABEL'], plan['PLANID']) for plan in plans])
show('Plans', formatted)
