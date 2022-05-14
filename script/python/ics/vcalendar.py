import typing

from . import BaseIcsObject


class VCalendar(BaseIcsObject):
    version: str
    objects: typing.List[BaseIcsObject]

    def __init__(self):
        self.version = "2.0"
        self.objects = []

    def get_data_list(self) -> typing.List[str]:
        result: typing.List[str] = []
        result.append("BEGIN:VCALENDAR")
        result.append("VERSION:" + self.version)
        for x in self.objects:
            result.extend(x.get_data_list())
        result.append("END:VCALENDAR")
        return result
