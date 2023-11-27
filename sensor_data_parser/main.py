from sensor_data_parser.arguments import ArgumentsRunner


def main() -> None:
    arguments_runner = ArgumentsRunner()
    arguments_runner.parse_arguments()
    arguments_runner.run_commands()


if __name__ == "__main__":
    main()
