import datetime
import typing

from . import BaseIcsObject
from . import STATUS, TRANSP


class VEvent(BaseIcsObject):
    dtstart: datetime.date
    dtend: datetime.date
    clas: str
    status: STATUS
    transp: TRANSP
    summary: str

    def get_data_list(self) -> typing.List[str]:
        result: typing.List[str] = []
        result.append("BEGIN:VEVENT")
        result.append("DTSTART;VALUE=DATE:" + self.dtstart.strftime("%Y%m%d"))
        result.append("DTEND;VALUE=DATE:" + (self.dtend + datetime.timedelta(days=1)).strftime("%Y%m%d"))
        result.append("SUMMARY:" + self.summary)
        result.append("STATUS:" + self.status.value)
        result.append("TRANSP:" + self.transp.value)
        result.append("END:VEVENT")
        return result
