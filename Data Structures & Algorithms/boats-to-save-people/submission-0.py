class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0, len(people) -1
        sorted_people = sorted(people)

        boats = 0

        while r >= l:
            boats += 1
            if sorted_people[l] + sorted_people[r] <= limit:
                l += 1
            r -= 1

        return boats

