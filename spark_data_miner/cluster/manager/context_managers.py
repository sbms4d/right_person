#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextlib import contextmanager

from spark_data_miner.cluster.manager.access import ClusterManager, ClusterPlan
from spark_data_miner.cluster.manager.session import get_new_right_person_spark_session
from spark_data_miner.cluster.ami.constants import NAME_FORMAT
from spark_data_miner.cluster.ami.utils import ami_exists
from spark_data_miner.cluster.utils import describe_ec2_properties_from_instance, add_package_to_spark, \
    get_instance_memory


@contextmanager
def spark_data_mining_session(plan):
    """
    creates a spark session to a temporary cluster
    :type plan: ClusterPlan
    """
    region = describe_ec2_properties_from_instance().region
    assert ami_exists(region), 'A valid AMI does not exist in this region ({})'.format(NAME_FORMAT.format('*'))
    instance_memory = get_instance_memory(plan.node_type)
    assert instance_memory >= 4, 'each spark node instance requires 4 GiB of memory'
    with ClusterManager(plan=plan) as inventory:
        master_ip = inventory['cluster_master']['PrivateIpAddress']
        useable_memory = int(round((instance_memory - 3) * 0.9, 0))  # TODO: parameterise
        session = get_new_right_person_spark_session(master_ip, useable_memory)
        add_package_to_spark(session, 'spark_data_miner')
        yield session


__all__ = ['spark_data_mining_session']
