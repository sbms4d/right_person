#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Config class(es) for the right person machine_learning
config contains information about good and normal data signatures as well as their ratios.
- RightPersonModelConfig to contain all of the signature information
- ModelSignatureFilter contains information specific to the
    signature (what fields and what values need to be set to be good etc)

These classes should only be used by the RightPersonModel class
"""
from __future__ import unicode_literals

from right_person.config.base_classes import AttributeCleaningMetaclass


class RightPersonModelConfig(object):
    """A configuration for a right_person machine_learning"""
    __metaclass__ = AttributeCleaningMetaclass

    def __init__(self, good_signature, normal_signature, max_ratio):
        """
        :param list[SignatureFilter] good_signature: the definition of good (any filters can pass to be included)
        :param list[SignatureFilter] normal_signature: the definition of normal
        :param float max_ratio: the maximum ratio of normal / good for machine learning machine_learning building
        """
        self.good_signature = good_signature  # tag_id = 1 for example
        self.normal_signature = normal_signature  # geo, is_mobile, etc
        self.max_ratio = max_ratio

    @staticmethod
    def clean_good_signature(signature_filters):
        try:
            return [f if isinstance(f, ModelSignatureFilter) else ModelSignatureFilter(**f) for f in signature_filters]
        except:
            raise ValueError('invalid traits! should be list of {}'.format(ModelSignatureFilter.__name__))

    @staticmethod
    def clean_normal_signature(signature_filters):
        try:
            return [f if isinstance(f, ModelSignatureFilter) else ModelSignatureFilter(**f) for f in signature_filters]
        except:
            raise ValueError('invalid filter conditions! should be list of {}'.format(ModelSignatureFilter.__name__))

    @staticmethod
    def clean_max_ratio(max_ratio):
        try:
            return float(max_ratio)
        except:
            raise ValueError('max ratio should be a float {}'.format(max_ratio))


class ModelSignatureFilter(object):
    """
    Defines a filter for a signature definition
    Either describes a filter in generating a list of good profile_ids (good signature)
    or a filter for refining the profiles (normal signature)
    """
    __metaclass__ = AttributeCleaningMetaclass

    def __init__(self, field_name, field_value, record_max_age=None):
        """
        the field name which is being filtered
        :param str field_name: the field_name to filter on
        :param str field_value:
        :param record_max_age:
        """
        self.field_name = field_name
        self.field_value = field_value
        self.record_max_age = record_max_age

    @staticmethod
    def clean_field_name(field_name):
        try:
            return str(field_name)
        except:
            raise ValueError('field_name must be a string! {}'.format(field_name))

    @staticmethod
    def clean_record_max_age(record_max_age):
        if record_max_age is None:
            return record_max_age
        if isinstance(record_max_age, int) and record_max_age >= 1:
            return record_max_age
        raise ValueError('record_max_age must be positive integer!')
