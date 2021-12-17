import argparse
import re
import subprocess
import sys

class Helper:
    def __init__(self, date, name):
        self.filepath = sys.argv[0]
        self.date = date
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
            ["python3", self.filepath, "--testing"],
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

    def get_inp(self):
        if self.args.testing:
            return False
        return "5"
