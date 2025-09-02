class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()  

        i = j = 0

        max_radius = 0

        while i < len(houses):
            while j < len(heaters) - 1 and abs(heaters[j] - houses[i]) >= abs(heaters[j+1] - houses[i]):
                j += 1

            if abs(houses[i] - heaters[j]) > max_radius:
                max_radius = abs(houses[i] - heaters[j])
            i += 1

        return max_radius
        