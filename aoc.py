import argparse
import datetime
import os
import pathlib
import platform
import re
import requests
import subprocess
import sys
import time

ANSI_RESET = "\x1b[0m"
ANSI_BOLD = "\x1b[1m"
ANSI_RED_BG = "\x1b[48;5;1m\x1b[38;5;0m"
ANSI_GREEN_BG = "\x1b[48;5;2m\x1b[38;5;0m"
ANSI_BLUE_BG = "\x1b[48;5;12m\x1b[38;5;0m"
ANSI_ORANGE_BG = "\x1b[48;5;3m\x1b[38;5;0m"

PREFIX_ERROR = ANSI_RED_BG + " ERROR " + ANSI_RESET
PREFIX_INFO = ANSI_BLUE_BG + " INFO " + ANSI_RESET
PREFIX_WARN = ANSI_ORANGE_BG + " WARNING " + ANSI_RESET

_SYSTEM= platform.system()
if _SYSTEM == "Windows":
    # Enable ansi escape colours for some Windows terminals.
    os.system("color")
    _PYCMD = "python"
else:
    _PYCMD = "python3"

class Helper:
    def __init__(self, date, name):
        self.filepath = sys.argv[0]

        m = re.search("(\d{2}|\d{4})\s*[/:]\s*(\d{1,2})", date)
        self.year, self.day = [int(g) for g in m.groups()]
        self.name = name

        print(f"--- Day {self.day}: {self.name} ---")

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
            [_PYCMD, self.filepath, "--testing"],
            input=sample.encode(),
            capture_output=True
        )
        if result.stderr:
            print("ERROR RUNNING SAMPLE INPUT:")
            print(result.stderr.decode())

        output = result.stdout.decode().replace("\r", "")
        answers = [str(i) for i in answers]

        p1 = re.search("Part ?1[: ] ?(.*?)\n", output, flags=re.IGNORECASE)
        if p1:
            ans = p1.groups()[0]
            if ans == str(answers[0]):
                print(ANSI_GREEN_BG, "PASSED", ANSI_RESET, 
                    f"Correct sample output ({ans!r} == {answers[0]!r})!"
                )
            else:
                print(ANSI_RED_BG, "FAILED", ANSI_RESET, 
                    f"Sample output {ans!r} does not match expected {answers[0]!r}."
                )


        p2 = re.search("Part ?2[: ] ?(.*?)\n", output, flags=re.IGNORECASE)
        if p2:
            ans = p2.groups()[0]
            if ans == str(answers[1]):
                print(ANSI_GREEN_BG, "PASSED", ANSI_RESET, 
                    f"Correct sample output ({ans!r} == {answers[1]!r})!"
                )
            else:
                print(ANSI_RED_BG, "FAILED", ANSI_RESET, 
                    f"Sample output {ans!r} does not match expected {answers[1]!r}."
                )
        
        print()

    def get_input(self, overwrite_cache=False):
        """Get input for the current puzzle.
        
        If there is a file input from stdin, use that. Otherwise,
        read from cached input or request input data from adventofcode.com
        and cache.

        Returns:
            The input string, unprocessed.
        """

        remaining = self.check_time()
        if isinstance(remaining, datetime.timedelta):
            print(PREFIX_ERROR, 
                f"Puzzle not unlocked, {str_timedelta(remaining)} remaining."
            )
            exit(0)

        if not sys.stdin.isatty():
            return sys.stdin.read()
        
        fp = pathlib.Path(
            f"~/.cache/adventofcode/{self.year:04}/{self.day:02}/input"
        ).expanduser()

        if not fp.is_file() or overwrite_cache:
            print(PREFIX_INFO, "Downloading input from adventofcode.com...\n")
            inp_s = self._request_inp()

            pathlib.Path.mkdir(fp.parent, parents=True, exist_ok=True)
            with open(fp, "w") as f:
                f.write(inp_s)
        else:
            with open(fp, "r") as f:
                inp_s = f.read()
        return inp_s

    def _request_inp(self):
        # Attempt to get session token from environment variables.
        _token = os.getenv("AOC_TOKEN")

        # Try to find token in some files if not found.
        if _token is None:
            paths = [
                ".AOC_TOKEN",
                ".AOC_SESSION",
                "~/.AOC_TOKEN",
                "~/.AOC_SESSION",
            ]
            for p in paths + [s.lower() for s in paths]:
                token_path = pathlib.Path(p).expanduser()
                if token_path.is_file():
                    with open(token_path, "r") as f:
                        _token = f.read().strip()
                    break
            else:
                print(PREFIX_ERROR + "Session token not found.")
                sys.exit(1)
        

        r = requests.get(
            f"https://adventofcode.com/{self.year}/day/{self.day}/input",
            headers={
                "User-Agent": "https://github.com/r-k-g/advent-of-code",
                "Cookie": f"session={_token}"
            }
        )

        assert r.status_code == 200

        return r.text

    def check_time(self):
        """Check if the current puzzle has unlocked.
        
        If there are less than 20 seconds left, wait.

        Returns:
            True if it has unlocked, False otherwise
        """

        est = datetime.timezone(datetime.timedelta(hours=-5))
        unlock = datetime.datetime(self.year, 12, self.day, tzinfo=est)
        now = datetime.datetime.now(tz=est)
        
        if now > unlock:
            return True
        
        delta = unlock - now
        if delta.seconds <= 20:
            print(PREFIX_INFO, 
                f"{delta.seconds} seconds remaining, sleeping..."
            )
            time.sleep(delta.seconds)
            return True
        else:
            return delta

def str_timedelta(delta):
    """Well, it works."""

    days = f"{delta.days} day{'s' * (delta.days > 1)}," * (delta.days > 0)
    hours, remainder = divmod(delta.seconds, 3600)
    hours = f"{hours} hour{'s' * (hours > 1)}," * (hours > 0)
    minutes, remainder = divmod(remainder, 60)
    minutes = f"{minutes} minute{'s' * (minutes > 1)}," * (minutes > 0)
    seconds = f"{remainder} second{'s' * (remainder > 1)}" * (remainder > 0)

    full = [unit for unit in [days, hours, minutes, seconds] if unit]
    full.insert(-1, "and")

    return " ".join(full)
