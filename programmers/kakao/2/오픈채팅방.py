def solution(record):
    answer = []
    users = {}
    log = []
    for r in record:
        part = r.split(" ")
        uid = part[1]
        if part[0] == "Enter":
            log.append((uid, "E"))
            users[uid] = part[2]
        elif part[0] == "Leave":
            log.append((uid, "L"))
        else:
            log.append((uid, "C"))
            users[uid] = part[2]
    print(log, users)

    for l in log:
        if l[1] == "E":
            answer.append(f'{users[l[0]]}님이 들어왔습니다.')
        elif l[1] == "L":
            answer.append(f'{users[l[0]]}님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))