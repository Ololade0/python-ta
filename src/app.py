import sys
import os


def prime(s):
    if s > 1:
        for i in range(2, s):
            if s % i == 0:
                return False

    return True

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
