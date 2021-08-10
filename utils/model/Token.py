id_ = 0


class Token:
    def __init__(self, name: str) -> None:
        global id_
        self._name = name
        self._id = id_
        id_ += 1

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id
