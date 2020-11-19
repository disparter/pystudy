# Implement an algorithm to determine if a string has all unique characters.
# Bonus: What if you cannot use additional data structures
import time


def is_unique(string):
    return False


if __name__ == '__main__':
    word = 'felipe is awesome'
    start = int(round(time.time() * 1000))
    result = is_unique(word)
    stop = int(round(time.time() * 1000))
    print('Time of execution: ', stop - start)
