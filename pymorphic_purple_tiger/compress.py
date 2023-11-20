from math import floor
from functools import reduce

def compress(bytes, target):

    length = len(bytes)
    assert target <= length, 'Fewer input bytes than requested output'

    # Calculate the segment size (divide and round down)

    seg_size = floor(length / target)

    # Split 'bytes' array into 'target' number of segments.

    i, segments = 0, []
    while i < target:
        start_point = i * seg_size
        end_point = length if i + 1 == target else (i + 1) * seg_size
        slice = bytes[start_point:end_point]
        segments.append(slice)
        i += 1

    return [reduce(lambda acc, curr: acc ^ curr, segment) for segment in segments]