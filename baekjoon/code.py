from collections import Counter

def solution(logs):
    answer = []
    problems = []
    users = set()
    logs = set(logs)
    logs = list(logs)
    for log in logs:
        name, problem = log.split()
        users.add(name)
        problems.append(problem)
    
    problems = Counter(problems)

    if len(users) % 2 == 0:
        half = int(len(users)//2)
    else:
        half = int(len(users)//2) + 1

    for pro in problems:
        if problems[pro] >= half:
            answer.append(pro)

    answer.sort()
    return answer


print(solution(["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]))
# ["reverse", "stng_compare"]
print(solution(["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"])) 
# ["sort"]
print(solution(["kate sqrt"]))  
# ["sqrt"]