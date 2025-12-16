from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


class ResultType(Enum):
    SUCCESS = auto()
    ERROR = auto()
    UNKNOWN = auto()


@dataclass
class Result:
    result_type: ResultType = field(init=True, repr=True)
    result: Any = field(init=True, repr=False)
    msg: str = field(init=True, default_factory=str, repr=True)
    msg_details: list = field(init=True, default_factory=list, repr=False)
    msg_details_delimiter: str = field(init=True, default_factory=str, repr=True)

    @property
    def message(self):
        result = f"{self.result_type.name} : {self.msg}"

        if self.msg_details:
            result += f": {self.msg_details_delimiter.join(self.msg_details)}"


@dataclass
class Results:
    results: dict = field(init=False, default_factory=dict, repr=True)

    @property
    def result_types(self) -> set:
        return {result.result_type for result in self.results}

    def all_result_type(self, result_type: ResultType) -> bool:
        return self.result_types == set([result_type])

    def any_result_type(self, result_type: ResultType) -> bool:
        return result_type in self.result_types

    def result_type_messages(self, result_type: ResultType):
        message = [obj.message for obj in self.results.values() if obj.result_type is result_type]
        return "||".join(message)
