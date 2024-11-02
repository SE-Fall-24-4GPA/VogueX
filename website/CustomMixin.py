# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

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
