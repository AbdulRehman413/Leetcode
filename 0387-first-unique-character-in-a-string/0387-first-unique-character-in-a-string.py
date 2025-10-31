class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = []        
        count = {}         
        front = 0       
        for i, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            queue.append((ch, i))   

            
            while front < len(queue) and count[queue[front][0]] > 1:
                front += 1   

        
        return queue[front][1] if front < len(queue) else -1