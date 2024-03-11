def find_intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if there is no intersection
    if end1 < start2 or end2 < start1:
        return None

    # Calculate the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    return (intersection_start, intersection_end)