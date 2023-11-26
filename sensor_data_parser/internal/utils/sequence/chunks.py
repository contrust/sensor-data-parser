from collections.abc import Sequence


def chunks(sequence: Sequence, chunk_size: int):
    for i in range(0, len(sequence), chunk_size):
        yield sequence[i: i + chunk_size]
