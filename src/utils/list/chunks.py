from collections.abc import Sequence


def chunks(lst: Sequence, n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]
