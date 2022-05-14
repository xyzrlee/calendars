import typing


class BaseIcsObject:
    def get_data_list(self) -> typing.List[str]:
        raise NotImplementedError()
