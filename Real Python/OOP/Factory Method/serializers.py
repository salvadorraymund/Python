import json


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        # the code below is an example of an interface
        # .serialize() doesn't exist in this module can be accessed by the serializable argument
        serializable.serialize(serializer)
        return serializer.to_str()


class SerializeFactory:
    # create a dictionary of the formats you want to support
    # having an init method lets you create an instance (instansiate); see line 45
    def __init__(self):
        self._creators = {}

    # assign k.v pairs to your dictionary
    # key is the format, value is the Serializer class (i.e JsonSerializer, or XMLSerializer)
    def register_format(self, format, creator):
        self._creators[format] = creator

    # use the get method of a dictionary to return the serializer class of your choice
    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializeFactory()
factory.register_format('JSON', JsonSerializer)
