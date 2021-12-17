import sys

import runner

args = runner.handle_args()

SAMPLE = "1"
runner.check_sample(args.test, SAMPLE)

IN = runner.get_inp(args) or sys.stdin.read()

n = 1 * int(IN.strip())
print("Part 1:", n)
print("Part 2:", -n)