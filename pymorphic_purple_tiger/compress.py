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
        if i + 1 == target:
            end_point = length  # Catch any left-over bytes in the last segment.
        else:
            end_point = (i + 1) * seg_size
        slice = bytes[start_point:end_point]
        segments.append(slice)
        i += 1

    checksums = [reduce(lambda acc, curr: acc ^ curr, segment) for segment in segments]


    return checksums