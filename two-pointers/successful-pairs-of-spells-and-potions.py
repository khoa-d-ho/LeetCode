class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = [(spell, index) for index, spell in enumerate(spells)]

        sortedSpells.sort()
        potions.sort()

        pairs = [0] * len(spells)
        
        m = len(potions)

        potion_index = len(potions) - 1
        for spell, index in sortedSpells:
            while potion_index >= 0 and potions[potion_index] * spell >= success:
                potion_index -= 1

            pairs[index] = m - potion_index - 1

        return pairs