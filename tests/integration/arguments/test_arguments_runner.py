from io import StringIO

import pytest
import sqlalchemy
from _pytest.fixtures import FixtureRequest
from sqlalchemy import Engine

from sensor_data_parser.arguments import ArgumentsRunner
from sensor_data_parser.internal.parsers import HexStringParser


@pytest.fixture()
def stream_input(request: FixtureRequest) -> str:
    if hasattr(request, "param"):
        return request.param
    raise NotImplementedError


@pytest.fixture()
def argument_runner(engine: Engine) -> ArgumentsRunner:
    runner = ArgumentsRunner()
    runner._engine = engine
    runner._set_engine = lambda *_: None
    return runner


@pytest.fixture()
def argument_runner_with_mocked_stream(
        argument_runner,
        stream_input) -> ArgumentsRunner:
    argument_runner._stream = StringIO(stream_input)
    return argument_runner


def test_creates_tables_when_creates_tables_option(engine, argument_runner):
    argument_runner.parse_arguments(['--create-tables'])
    argument_runner.run_commands()
    assert sqlalchemy.inspect(engine).has_table('pressure_packet')


@pytest.mark.parametrize('stream_input',
                         ('34ffffff80490000804a0000804b'
                          '0000804c0000804d000079f3ffff',))
def test_saves_packets_parsed_packets(
        argument_runner_with_mocked_stream,
        pressure_packet_repository,
        stream_input):
    argument_runner_with_mocked_stream.parse_arguments([])
    argument_runner_with_mocked_stream.run_commands()
    packets = HexStringParser(stream_input).to_pressure_packets()
    for i in range(len(packets)):
        packet = packets[i]
        db_packet = pressure_packet_repository.get(i + 1)
        assert db_packet
        assert packet.current_value_counter == db_packet.current_value_counter
        assert packet.status == db_packet.status
        assert packet.pressure_value == db_packet.pressure_value


@pytest.mark.parametrize('stream_input', ('80000000',))
def test_does_not_raise_exception_when_no_db_tables(
        argument_runner_with_mocked_stream, stream_input):
    argument_runner_with_mocked_stream.parse_arguments()
    argument_runner_with_mocked_stream.run_commands()
