class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        temp_arr = []

        for num in nums:
            # Add num to temp_arr if it's empty or the difference condition is met
            if not temp_arr or num - temp_arr[0] <= k:
                temp_arr.append(num)

                # If temp_arr has reached size 3, add it to the result and reset it
                if len(temp_arr) == 3:
                    result.append(temp_arr)
                    temp_arr = []
            else:
                # If the condition is not met, it's impossible to satisfy the requirements
                return []    
        return result
