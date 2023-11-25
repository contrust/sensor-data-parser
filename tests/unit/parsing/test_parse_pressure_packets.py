import pytest

from src.parsing.parse_pressure_packets import parse_pressure_packets


@pytest.mark.parametrize("data", ("80ff0000", "79000000"))
def test_parse_pressure_packets_does_not_return_invalid_models(data: str):
    assert parse_pressure_packets(data) == []


@pytest.mark.parametrize("data", ("80000000",))
def test_parse_pressure_packets_returns_valid_models(data: str):
    assert len(parse_pressure_packets(data)) == 1


@pytest.mark.parametrize("data", ("800000007900000080010000",))
def test_parse_pressure_packets_continues_parsing_after_failed_parsing(
    data: str,
):
    assert len(parse_pressure_packets(data)) == 2
