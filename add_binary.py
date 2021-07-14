class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_i = len(a) - 1
        b_i = len(b) - 1
        
        result = ''
        add = 0
        
        while a_i >= 0 and b_i >= 0:
            sum = (int(a[a_i]) + int(b[b_i]) + add) % 2
            add = (int(a[a_i]) + int(b[b_i]) + add) // 2
            result += str(sum)
            a_i -= 1
            b_i -= 1
            
        if a_i >= 0:
            while a_i >= 0:
                sum = (int(a[a_i]) + add) % 2
                add = (int(a[a_i]) + add) // 2
                result += str(sum)
                a_i -= 1
                
        if b_i >= 0:
            while b_i >= 0:
                sum = (int(b[b_i]) + add) % 2
                add = (int(b[b_i]) + add) // 2
                result += str(sum)
                b_i -= 1        
        
        if add != 0:
            result += str(add)
                
        return result[::-1]
