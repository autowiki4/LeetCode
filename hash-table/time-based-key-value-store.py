from collections import defaultdict
class TimeMap:

    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) pair to the list for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Get the list of (timestamp, value) for the key
        if key not in self.store:
            return ""
        
        values = self.store[key]
        # Perform manual binary search for the largest timestamp <= given timestamp
        left, right = 0, len(values) - 1
        result = ""  # Default to empty string if no valid timestamp is found

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                # Found a candidate, move right to find the largest timestamp <= given timestamp
                result = values[mid][1]
                left = mid + 1
            else:
                # Timestamp is too large, move left
                right = mid - 1

        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)