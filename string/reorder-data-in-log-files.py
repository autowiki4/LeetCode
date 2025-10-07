class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def hasDigit(inputt):
            return any(char.isdigit() for char in inputt)

        letter_logs, digit_logs = [], []

        res = []

        for i in range(len(logs)):
            vals = logs[i].split()
            if hasDigit(vals[1:]):
                digit_logs.append(logs[i])
            else:
                letter_logs.append([' '.join(vals[1:]), vals[0], i])
        
        for log in sorted(letter_logs):
            res.append(logs[log[2]])
        
        return res + digit_logs