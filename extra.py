import random
import string
import log


# a file for misc commands
def keyGen(length=16, seed=hash(random)):

    seed = seed.__str__()
    key = ''.join(random.choices(string.ascii_uppercase + string.digits + seed, k=length))
    log.log("", "rand")
    return key


def printBanner():
    print(
        '  __      __            _                 \n'
        '  \\ \\    / /_ _ _ _  __| |___ _ _ ___ _ _\n'
        '   \\ \\/\\/ / _\\` | \' \\/ _` / -_) \'_/ -_) \'_|\n'
        '    \\_/\\_/\\__,_|_||_\\__,_\\___|_| \\___|_|  \n')
    log.log("banner", "output")
