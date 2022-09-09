"""For command options"""
import argparse


class ArgumentParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()

    def get_args(self):
        """Getting arguments for command"""
        self.parser.add_argument(
            "-r", "--root", required=True, type=str, default="./", help="Project root directory    ex) -r ./")
        self.parser.add_argument(
            "-p", "--histogram", required=False, default=True, type=bool, help="Print histogram    ex) -p False")
        self.parser.add_argument(
            "-o", "--output", required=False, type=str, help="Output file(json) path    ex) -o ./gla_output.json")
        self.parser.add_argument(
            "-a", "--after", required=False, type=str, help="After    ex) -a 2022-09-07")
        self.parser.add_argument(
            "-b", "--before", required=False, type=str, help="Before    ex) -b 2022-09-10")
        self.parser.add_argument(
            "-e", "--allowedext", required=False, type=str, nargs='+', help="Allowed extension    ex) -e py java c cpp"
        )

        return self.parser.parse_args()
