import heapq
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        free_rooms = [_ for _ in range(n)]
        heapq.heapify(free_rooms)
        per_room = [0] * n
        slots = sorted(meetings)
        in_prog = []

        i = 0
        while i < len(slots):
            slot = slots[i]
            # Release every room whose meeting has ended
            while in_prog and in_prog[0][0] <= slot[0]:
                end_time, room = heapq.heappop(in_prog)
                heapq.heappush(free_rooms, room)

            if free_rooms:                  
                # Take a room if there are free rooms   
                room = heapq.heappop(free_rooms)
                per_room[room] += 1
                heapq.heappush(in_prog, (slot[1],room))
                i += 1
                continue

            (earliest_end,freed_room) = heapq.heappop(in_prog)
            duration = slot[1] - slot[0]
            slot[0] = earliest_end
            slot[1] = earliest_end + duration
            per_room[freed_room] += 1
            heapq.heappush(in_prog, (slot[1],freed_room))
            i += 1

        return per_room.index(max(per_room))