from itertools import permutations, product
import re

from lib import *
problem = old_aoc.Problem("2021/19: Beacon Scanner")
problem.preprocessor = ppr.llsg

class Scanner:
    def __init__(self, number, beacons: set):
        axes = list(product([1, -1], repeat=3))
        indices = list(permutations([0,1,2]))
        self.orientations = list(product(axes, indices))

        self.number = number
        self.relative_beacons = beacons
        self.beacons = self.relative_beacons.copy()

        self.x = 0
        self.y = 0
        self.z = 0
    
    def beacons_from_starting(self, x, y, z):
        self.beacons = set((xr + x, yr + y, zr + z) for xr, yr, zr in self.beacons)

    def reset_beacons(self):
        self.beacons = self.relative_beacons.copy()

    def all_orientations(self):
        for axes, indices in self.orientations:
            new_beacons = set()
            for x, y, z in self.beacons:
                point = [x * axes[0], y * axes[1], z * axes[2]]
                new_beacons.add(tuple(point[i] for i in indices))
            self.beacons = new_beacons
            yield self.beacons

    def __repr__(self):
        return f"Scanner({self.number=}, {len(self.beacons)=})"
    
    def pprint(self):
        print(f"Scanner({self.number=}, self.beacons={{")
        for b in self.beacons:
            print(f"\t{b},")
        print("})")

def common_points(points1, points2):
    return points1 & points2

@problem.solver()
def solve(inp):
    scanners = []
    fixed = []

    for scanner in inp:
        number, *beacons = scanner
        number = int(re.match("--- scanner (\d+) ---", number).groups()[0])
        
        points = set()
        for beacon in beacons:
            x, y, z = map(int, beacon.split(","))
            points.add((x, y, z))
        
        scanners.append(Scanner(number, points))
    
    fixed.append(scanners.pop(0))
    b_map = fixed[0].beacons.copy()

    while scanners:
        found = False
        for sc in scanners:
            for beacons in sc.all_orientations():
                for beacon, final in product(beacons, b_map):
                    xdiff = final[0] - beacon[0]
                    ydiff = final[1] - beacon[1]
                    zdiff = final[2] - beacon[2]
                    sc.beacons_from_starting(xdiff, ydiff, zdiff)

                    if len(c := common_points(b_map, sc.beacons)) >= 12:
                        b_map = b_map | sc.beacons
                        scanners.remove(sc)
                        fixed.append(sc)
                        sc.x = xdiff
                        sc.y = ydiff
                        sc.z = zdiff
                        found = True
                        break
                    
                    # undo move
                    sc.beacons_from_starting(-xdiff, -ydiff, -zdiff)
                if found: break
                sc.reset_beacons()
            if found: break

    distances = []
    for s1, s2 in product(fixed, repeat=2):
        distances.append(
            abs(s1.x - s2.x) + abs(s1.y - s2.y) + abs(s1.z - s2.z)
        )

    return (len(b_map), max(distances))

SAMPLE_INP = ("""
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 79, 3621)