print("\n")
print("\n")
print("\t \t \t Reorder data logs")
class Solution(object):
    def reorderLogFiles(self, logs):
        def custom_sort(log):
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                # For digit-logs
                return (1, None, None)
            else:
                # For letter-logs
                return (0, content, identifier)

        sorted_logs = sorted(logs, key=custom_sort)
        return sorted_logs

solution = Solution()
# test log input
# ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

logs_input = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs_input2 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result = solution.reorderLogFiles(logs_input)
result2 = solution.reorderLogFiles(logs_input2)
print(result)    
print(result2)   


print("\n")
print("\n")