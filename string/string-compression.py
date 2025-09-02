class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        count = 1
        i = 1
        while i < len(chars):
            if chars[i] == chars[i - 1]:
                count += 1
                chars.pop(i)
                i -= 1
            else:
                if count == 1:
                    i += 1 
                    continue
                insert_chars = list(str(count))
                for j in range(len(insert_chars)):
                    chars.insert(i + j, insert_chars[j])
                i += len(insert_chars)
                count = 1
            i += 1
        if count == 1:
            return len(chars)
        insert_chars = list(str(count))
        for j in range(len(insert_chars)):
            chars.insert(i + j, insert_chars[j])
        return len(chars)


                    
            