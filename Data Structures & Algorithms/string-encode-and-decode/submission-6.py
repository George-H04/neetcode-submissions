class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            encoded_str += str(len(string)) + "^" + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        string_list = []

        i = 0
        while i < len(s):
            j = s.find("^", i)

            length = int(s[i:j])

            i = j + 1

            string_list.append(s[i : i + length])

            i += length

        return string_list
       
