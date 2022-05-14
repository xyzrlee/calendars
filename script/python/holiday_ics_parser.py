import datetime
import getopt
import os
import sys
import typing

import yaml

import ics


class HolidayIcsParser:
    __config_file_dir: str
    __holidays: list

    def __init__(self, config_file_dir: str):
        self.__holidays = []
        self.__config_file_dir = config_file_dir
        self._read_files()

    def _read_files(self):
        it: list
        with os.scandir(self.__config_file_dir) as it:
            entry: os.DirEntry
            for entry in it:
                if not entry.is_file(): continue
                if not entry.name.endswith(".yaml"): continue
                fn: str = os.path.join(self.__config_file_dir, entry.name)
                with open(fn, "r") as inf:
                    data: dict = yaml.load(inf, Loader=yaml.FullLoader)
                    if isinstance(data, dict) and "holidays" in data:
                        holidays: list = data.get("holidays")
            print(holidays)
            self.__holidays.extend(holidays)

    def write_to_file(self, output_file):
        vcalendar = ics.VCalendar()
        vcalendar.version = "2.0"
        holiday: dict
        for holiday in self.__holidays:
            if not isinstance(holiday, dict):
                continue
            vevent = ics.VEvent()
            vevent.dtstart = holiday.get("start")
            vevent.dtend = holiday.get("end")
            vevent.summary = holiday.get("name")
            vevent.status = ics.STATUS.CONFIRMED
            vevent.transp = ics.TRANSP.TRANSPARENT
            vcalendar.objects.append(vevent)
            if "changes" in holiday:
                changes: list
                changes = holiday.get("changes")
                if isinstance(changes, list):
                    x: datetime.date
                    for x in changes:
                        change_vevent = ics.VEvent()
                        change_vevent.dtstart = x
                        change_vevent.dtend = x
                        change_vevent.summary = "调休"
                        change_vevent.status = ics.STATUS.CONFIRMED
                        change_vevent.transp = ics.TRANSP.TRANSPARENT
                        vcalendar.objects.append(change_vevent)
        data: typing.List[str] = vcalendar.get_data_list()
        with open(output_file, "w") as ouf:
            for x in data:
                print(x, file=ouf, sep="\r\n")


if __name__ == "__main__":
    config_dir: str = ""
    output_file: str = ""
    opts, args = getopt.getopt(sys.argv[1:], "", ["config-dir=", "output-file="])
    for opt, arg in opts:
        if opt == "--output-file":
            output_file = arg
        elif opt == "--config-dir":
            config_dir = arg

    parser: HolidayIcsParser = HolidayIcsParser(config_dir)
    parser.write_to_file(output_file)
