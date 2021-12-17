import argparse
import re
import subprocess

def handle_args():
    parser = argparse.ArgumentParser(description="Solve some AOC!")
    parser.add_argument("-t", "--test", action="store_true",
        help="Flag for testing to not give default input or test again.")
    args = parser.parse_args()
    return args

def check_sample(test, sample):
    if test: # Already testing!
        return
    
    result = subprocess.run(
        ["python", "test.py", "--test"],
        input=sample.encode(),
        capture_output=True
    )
    if result.stderr:
        print("ERROR RUNNING SAMPLE INPUT:")
        print(result.stderr.decode())

    output = result.stdout.decode().replace("\r", "")

    p1 = re.search("Part ?1[: ] ?(.*?)\n", output, flags=re.IGNORECASE)
    if p1:
        print("P1", p1.groups()[0])

    p2 = re.search("Part ?2[: ] ?(.*?)\n", output, flags=re.IGNORECASE)
    if p2:
        print("P2", p2.groups()[0])
    
    print()

def get_inp(args):
    if args.test:
        return False
    return "5"
