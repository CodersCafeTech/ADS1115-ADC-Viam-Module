"""
This file registers the model with the Python SDK.
"""

from viam.components.generic import Generic
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .ads1115 import ads1115

Registry.register_resource_creator(Generic.SUBTYPE, ads1115.MODEL, ResourceCreatorRegistration(ads1115.new, ads1115.validate))
