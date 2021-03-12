import sys
script = sys.argv[0]

def printout():
        sys.exit(f'Usage: Python {script} pattern')

def main_function(argv):
        if len(argv) < 1:
            printout()

        if len(argv) == 1:
            pola = argv[0]
            for line in sys.stdin:
                if pola in line:
                    print(line.strip())

        if len(argv) > 1:
            baris = open(argv[1])
            pola = argv[0]
            for line in baris:
                if pola in line:
                     print(line.strip())

if __name__ == '__main__':
        main_function(sys.argv[1:])