#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'Zack Nagaich'
__copyright__ = 'Copyright 2016, Phishwatcher Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Zack Nagaich'
__email__ = 'zacknagaich@gmail.com'
__status__ = 'Development'

__all__ = [
    'PhishwatcherEntity',
    'MyPhishwatcherEntity'
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyPhishwatcherEntity will
have an entity type name of PhishWatcher.MyPhishwatcherEntity. When adding a new entity in Maltego, you will have to specify this
name (PhishWatcher.MyPhishwatcherEntity) in the 'Unique entity type' field.
"""
class PhishwatcherEntity(Entity):
    _namespace_ = 'PhishWatcher'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
    - is_value: a boolean value that determines whether the field is also the default value of the entity object.
TODO: define as many custom fields and entity types as you wish:)
"""    
@EntityField(name='PhishWatcher.fieldN', propname='fieldN', displayname='Field N', matchingrule=MatchingRule.Loose)
@EntityField(name='PhishWatcher.field1', propname='field1', displayname='Field 1', type=EntityFieldType.Integer)
class MyPhishwatcherEntity(PhishwatcherEntity):
    """
    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
    'my.fancy.EntityType'
    """
    # _name_ = 'my.fancy.EntityType'
    pass