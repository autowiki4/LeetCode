class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        if k == 0:
            return
        cycles = math.gcd(n, k)
        
        for start in range(cycles):
            current = start
            prev = nums[start]
            
            while True:
                next_pos = (current + k) % n
                nums[next_pos], prev = prev, nums[next_pos]
                current = next_pos
                
                if current == start:
                    break
        