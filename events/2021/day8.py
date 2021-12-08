from lib import *
problem = aoc.Problem("2021/08: Seven Segment Search")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    unique_segcount_to_num = {2: 1, 4: 4, 3: 7, 7: 8}

    outputs = []

    for v in inp:
        v = v.split(" | ")
        patterns, output = [group.split() for group in v]
        
        # part 1
        for i in output:
            if len(i) in [2, 4, 3, 7]:
                p1 += 1

        # part 2
        num_mappings = dict.fromkeys(range(10))
        for k in num_mappings:
            num_mappings[k] = set("abcdefg")

        for i in output + patterns:
            if len(i) not in unique_segcount_to_num:
                continue
            
            number = unique_segcount_to_num[len(i)]
            num_mappings[number] &= set(i)
        
        for i in output + patterns:
            if len(i) in unique_segcount_to_num:
                continue
            
            if len(i) == 6:
                if len(set(i) & num_mappings[1]) == 1:
                    num_mappings[6] &= set(i)
                elif len(set(i) & num_mappings[4]) == 4:
                    num_mappings[9] &= set(i)
                else:
                    num_mappings[0] &= set(i)
            
            if len(i) == 5:
                if len(set(i) & num_mappings[1]) == 2:
                    num_mappings[3] &= set(i)
                elif len(set(i) & num_mappings[4]) == 2:
                    num_mappings[2] &= set(i)
                elif len(set(i) & num_mappings[4]) == 3:
                    num_mappings[5] &= set(i)
        
        letters_to_nums = {frozenset(v): k for k, v in num_mappings.items()}

        translated_out = []
        for seg_group in output:
            translated_out.append(str(letters_to_nums[frozenset(seg_group)]))

        outputs.append(int("".join(translated_out)))

    return (p1, sum(outputs))

SAMPLE_INP =\
"""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 26, 61229)