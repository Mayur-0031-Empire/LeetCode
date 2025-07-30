class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_index = 0
        count = 1
        curr_char = chars[0]
        for i in range(1, len(chars)):
            if chars[i] != curr_char:
                if count != 1:
                    chars[curr_index] = curr_char
                    curr_index += 1
                    str_count = str(count)
                    for c in str_count:
                        chars[curr_index] = c
                        curr_index += 1
                    count = 1
                else :
                    chars[curr_index] = curr_char
                    curr_index += 1
                curr_char = chars[i]
            else :
                count += 1
        if count != 1:
            chars[curr_index] = curr_char
            curr_index += 1
            str_count = str(count)
            for c in str_count:
                chars[curr_index] = c
                curr_index += 1
            count = 1
        else :
            chars[curr_index] = curr_char
            curr_index += 1         
        return curr_index
                


