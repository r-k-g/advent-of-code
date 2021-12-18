import argparse
import os
import pathlib
import re
import requests
import subprocess
import sys

class Helper:
    def __init__(self, date, name):
        self.filepath = sys.argv[0]

        m = re.search("(\d{2}|\d{4})\s+[/:]\s+(\d{1,2})", date)
        self.year, self.day = [int(g) for g in m.groups()]
        self.name = name

        self.handle_args()

    def handle_args(self):
        parser = argparse.ArgumentParser(description="Solve some AOC!")
        parser.add_argument("--testing", action="store_true",
            help="Flag for testing to not give default input or test again.")
        self.args = parser.parse_args()

    def check_sample(self, sample, *answers):
        if self.args.testing: # Already testing!
            return
        
        result = subprocess.run(
            ["python", self.filepath, "--testing"],
            input=sample.encode(),
            capture_output=True
        )
        if result.stderr:
            print("ERROR RUNNING SAMPLE INPUT:")
            print(result.stderr.decode())

        output = result.stdout.decode().replace("\r", "")
        
        with open("temp.txt", "w") as f:
            f.write(output)

        p1 = re.search("Part ?1[: ] ?(.*?)\n", output, flags=re.IGNORECASE)
        if p1:
            print("P1", p1.groups()[0])

        p2 = re.search("Part ?2[: ] ?(.*?)\n", output, flags=re.IGNORECASE)
        if p2:
            print("P2", p2.groups()[0])
        
        print()

    def get_input(self):
        _token = os.getenv("AOC_TOKEN")
        if _token is None:
            token_fp = None
            paths = [
                ".AOC_TOKEN",
                ".AOC_SESSION",
                "~/.AOC_TOKEN",
                "~/.AOC_SESSION",
            ]
            for p in paths:
                path = pathlib.Path(p).expanduser()
                if path.is_file():
                    token_fp = path
                    break
            if token_fp is not None:
                pass
            else:
                pass
        
        r = requests.get(
            f"https://adventofcode.com/{self.year}/day/{self.day}/input",
            headers={
                "User-Agent": "https://github.com/r-k-g/advent-of-code",
                "Cookie": f"session={_token}"
            }
        )
        if self.args.testing:
            return False
        return "5"
