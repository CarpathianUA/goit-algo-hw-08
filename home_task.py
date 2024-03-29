import heapq


def connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)

    total = 0

    while len(cable_lengths) > 1:
        first_piece = heapq.heappop(cable_lengths)
        second_piece = heapq.heappop(cable_lengths)

        cable_cost = first_piece + second_piece
        total += cable_cost

        heapq.heappush(cable_lengths, cable_cost)

    return total


cable_lengths = [5, 2, 4, 7, 3, 9, 22, 1, 6, 8]
print(connect_cables(cable_lengths))
