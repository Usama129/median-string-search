import sys
from medianString import bounded_median_string

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    arr = contents.splitlines()
    k = arr.pop(0)

    if int(k) > 16 or int(k) < 1:
        print('Invalid length specified. Pattern length must be equal to or less than 16.')
        sys.exit()

    if len(arr) > 100:
        print('Input exceeds maximum number of DNA sequences. Sequences must be 100 or lower.')
        sys.exit()

    if len(arr[0]) > 500:
        print('Sequence lengths exceed the maximum supported length of 500.')
        sys.exit()

    print("Running a Bounded Median String search on", sys.argv[1],"...")
    consensus = bounded_median_string(arr, len(arr), len(arr[0]), int(k))
    print("*** Consensus is", consensus, "***")

    with open("output.txt", 'w') as o:
        o.write(consensus)
        print("Consensus string written to output.txt")

