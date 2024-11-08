class Solution:
    def roman_to_integer(self, s: str) -> int:
      
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s): 
            current_value = roman_dict[char]
           
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value  

        return total


solution = Solution()
roman_numeral = input("Give a number in Roman numerals (I / V / X / L / C / D / M): ").strip().upper()
result = solution.roman_to_integer(roman_numeral)
print(f"The integer value is: {result}")