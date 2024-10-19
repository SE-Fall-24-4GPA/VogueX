from sqlalchemy.inspection import inspect

"""
Class to serialize the SQLALchemy Object to a json object
"""


class SerializerMixin(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(elements):
        return [m.serialize() for m in elements]
