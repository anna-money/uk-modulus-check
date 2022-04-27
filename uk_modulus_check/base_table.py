import abc


class BaseTable(abc.ABC):
    @abc.abstractmethod
    def load(self, lines: list[str]) -> None:
        ...
