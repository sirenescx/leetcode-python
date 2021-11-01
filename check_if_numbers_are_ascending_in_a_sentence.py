class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        previous_number: int = -1
        current_number: int = -1
        number_string: str = ''
        for char in s:
            if char.isdigit():
                number_string += char
            else:
                if number_string != '':
                    current_number = int(number_string)
                    if previous_number == -1:
                        previous_number = int(number_string)
                    else:
                        if current_number <= previous_number:
                            return False
                        previous_number = current_number
                    number_string = ''
                    
        if number_string != '':
            if int(number_string) <= previous_number:
                return False            
        
        return True
