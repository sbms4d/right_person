#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextlib import contextmanager

from spark_data_miner.cluster.manager.access import ClusterManager
from spark_data_miner.cluster.manager.session import get_new_right_person_spark_session
from spark_data_miner.cluster.ami.constants import NAME_FORMAT
from spark_data_miner.cluster.ami.utils import ami_exists
from spark_data_miner.cluster.utils import describe_ec2_properties_from_instance


@contextmanager
def spark_data_mining_session(plan):
    region = describe_ec2_properties_from_instance().region
    assert ami_exists(region), 'A valid AMI does not exist in this region ({})'.format(NAME_FORMAT.format('*'))
    with ClusterManager(plan=plan) as inventory:
        master_ip = inventory['cluster_master']['PrivateIpAddress']
        yield get_new_right_person_spark_session(master_ip)


__all__ = ['spark_data_mining_session']
