import datetime
import os
import pathlib
import re
import requests
import sys
import time

class Problem:
    """ class Problem

    Represents and provides methods relating to a single Advent of Code
    problem.
    """

    def __init__(self, *args, **kwargs):
        """ __init__()

        Pass the year, month, and problem name to the constructor to
        instantiate a new Problem.

            Problem("2015/01: Not Quite Lisp")
            Problem(year=2015, day=1, name="Not Quite Lisp")
        """

        match = re.fullmatch(
            re.compile(
                r"(?P<year>[0-9]{4})\/"
                + r"(?P<day>0?[1-9]|1[0-9]|2[0-5])\: "
                + r"(?P<name>.+)"
            ),
            "".join(args),
        )

        if (match):
            self.year = int(match.group("year"))
            self.day = int(match.group("day"))
            self.name = str(match.group("name"))
        elif all(field in kwargs.keys() for field in ["year", "day", "name"]):
            self.year = int(kwargs.get("year", 0))
            self.day = int(kwargs.get("day", 0))
            self.name = str(kwargs.get("name", "???"))
        else:
            raise ValueError(
                "Could not parse arguments to Problem constructor."
            )

        # The solver functions, and the input preprocessor, are stored as class
        # fields.
        self.fns = {}
        self.preprocessor = lambda x: x

        # All tests are user-defined.
        self.tests = {}

    def solver(self, part="both"):
        """ solver()

        A decorator for a function to mark it as a solver function to run.
        Optionally specify the part being solved using the `part` keyword
        argument.
        """

        def register(fn):
            # Register the solver function in the instance dictionary variable
            # `self.fns`.
            self.fns[part] = fn
            return fn

        return register

    def solve(self, sample_inp=None, *sample_ans):
        """ solve()

        Run the solver functions and pretty-print the output.
        """

        print("--- Day {}: {} ---".format(self.day, self.name))

        inp_s = self._get_input()

        if inp_s is None: # no input
            return

        self.check_sample(sample_inp, sample_ans)

        # Run each solver.
        for part, fn in self.fns.items():
            # Apply the preprocessor.
            inp = self.preprocessor(inp_s)

            # Run the solver on the input and time the runtime.
            start = time.perf_counter()
            out = fn(inp)
            stop = time.perf_counter()

            # Compute runtime and appropriate time unit.
            delta, unit = (stop - start), 0
            while delta < 1 and unit <= 3:
                delta, unit = 1000 * delta, unit + 1
            delta, unit = round(delta, 5), ["s", "ms", "us", "ns"][unit]

            # Print answers
            if (part in ["both"]) and (type(out) is tuple) and (len(out) >= 2):
                print("Part 1: {}".format(out[0]))
                print("Part 2: {} (total runtime: {}{})".format(
                    out[1], delta, unit
                ))
            else:
                print("Part {}: {} (runtime: {}{})".format(
                    part, out, delta, unit
                ))
    
    def check_sample(self, sample_inp, sample_ans):
        """Check the sample input against expected output."""

        if sample_inp is not None and sample_inp.strip():
            if len(sample_ans) == 1 and type(sample_ans[0]) in (tuple, list):
                sample_ans = sample_ans[0]

            c = 0
            for part, fn in self.fns.items():
                s_inp = self.preprocessor(sample_inp)

                out = fn(s_inp)
                
                if not sample_ans:
                    print(f"Sample output: {out}")

                elif part in ["both"] and isinstance(out, tuple):
                    print(self._check_ans(out[0], sample_ans[0]))
                    print(self._check_ans(out[1], sample_ans[1]))
                
                else:
                    print(self._check_ans(out, sample_ans[c]))
                
                c += 1
    
    def _check_ans(self, out, expected):
        """Check if output matches expected value and return string explanation."""

        if out == expected:
            return f"\x1b[30;42m PASSED \x1b[0m Correct sample output ({out!r} == {expected!r})!"
        else:
            return f"\x1b[30;41m FAILED \x1b[0m Sample output {out!r} does not match expected {expected!r}."

    def _get_input(self):
        # Setup the path to the local cache.
        fp = pathlib.Path(
            "~/.cache/adventofcode/{:04}/{:02}/input".format(
                self.year, self.day
            )
        ).expanduser()

        if "--inp" in sys.argv or "--INP" in sys.argv:
            inp_l = []
            while True:
                i = input()
                if i.lower() == "!q":
                    break
                inp_l.append(i)
            inp_s = "\n".join(inp_l)

            if not fp.exists() or "--B" in sys.argv:
                # Write the response to the cache.
                fp.parent.mkdir(parents=True, exist_ok=True)
                with open(fp, "w") as fh:
                    fh.write(inp_s)

        # Fetch the input dynamically.
        elif not fp.exists() or "--B" in sys.argv:
            print("\x1b[30;44m INFO \x1b[0m Downloading input from adventofcode.com...")

            # First, check the current time to ensure that it is past midnight
            # before fetching problem input from server
            est = datetime.timezone(datetime.timedelta(hours=-5))
            delta = datetime.datetime(
                self.year, 12, self.day, tzinfo=est
            ) - datetime.datetime.now(tz=est)

            if datetime.timedelta(seconds=0) < delta <= datetime.timedelta(seconds=15):
                print("\x1b[30;44m INFO \x1b[0m Less than fifteen seconds remaining, will sleep...")
                sys.stdout.flush()
                time.sleep(delta.seconds + 1)

            elif delta > datetime.timedelta(seconds=0):
                # Determine time remaining until unlock and display a formatted
                # countdown timer.
                d = delta.days
                h = (delta.seconds // 3600) % 24
                m = (delta.seconds // 60) % 60
                s = (delta.seconds) % 60

                countdown = (
                    (f"{str(d).zfill(2)}d" if d > 0 else "")
                    + (f"{str(h).zfill(2)}h" if h > 0 else "")
                    + (f"{str(m).zfill(2)}m" if m > 0 else "")
                    + (f"{str(s).zfill(2)}s")
                )

                print("\x1b[30;41m FAIL \x1b[0m Problem hasn't unlocked;", countdown, "remaining.")
                return

            # Read the session token from an environment variable, or, if not
            # set, from a secret file.
            token = os.environ.get("AOC_TOKEN", None)
            if not token:
                with open(os.path.expanduser("~/.aoc/token"), "r") as fh:
                    token = fh.read()

            token = token.strip()

            # Fetch!
            r = requests.get(
                "https://adventofcode.com/{}/day/{}/input".format(
                    self.year, self.day
                ),
                headers={
                    "Cookie": f"session={token};",
                    # "User-Agent": "github/hughcoleman/advent-of-code",
                }
            )

            # Write the response to the cache.
            fp.parent.mkdir(parents=True, exist_ok=True)
            with open(fp, "w") as fh:
                fh.write(r.text)
            inp_s = r.text

            print("")

        else:
            # Read input from cache.
            with open(fp, "r") as fh:
                inp_s = fh.read()
        
        return inp_s

