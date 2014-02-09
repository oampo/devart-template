import math

U16_MAX = 2 ** 15 - 1

# Magic to interleave zeros in a 16 bit integer
def interleave(n):
    n &= 0x0000ffff
    n = (n | (n << 8)) & 0x00FF00FF
    n = (n | (n << 4)) & 0x0F0F0F0F
    n = (n | (n << 2)) & 0x33333333
    n = (n | (n << 1)) & 0x55555555
    return n

# Magic to deinterleave a 16 bit integer
def deinterleave(n):
    n &= 0x55555555
    n = (n ^ (n >> 1)) & 0x33333333
    n = (n ^ (n >> 2)) & 0x0f0f0f0f
    n = (n ^ (n >> 4)) & 0x00ff00ff
    n = (n ^ (n >> 8)) & 0x0000ffff
    return n

def encode(x, y, cellX, cellY):
    x = int(math.floor(x) / cellX + U16_MAX)
    y = int(math.floor(y) / cellY + U16_MAX)
    x = interleave(x)
    y = interleave(y)
    return x | y << 1


def decode(hash, cellX, cellY):
    x = (deinterleave(hash) - U16_MAX) * cellX + float(cellX) / 2
    y = (deinterleave(hash >> 1) - U16_MAX) * cellY + float(cellY) / 2
    return x, y

def neighbors(hash):
    x, y = decode(hash, 1, 1)
    return [encode(x - 1, y - 1, 1, 1),
            encode(x - 1, y, 1, 1),
            encode(x - 1, y + 1, 1, 1),
            encode(x, y - 1, 1, 1),
            encode(x, y + 1, 1, 1),
            encode(x + 1, y - 1, 1, 1),
            encode(x + 1, y, 1, 1),
            encode(x + 1, y + 1, 1, 1)]
