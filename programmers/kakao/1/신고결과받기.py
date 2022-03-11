from collections import defaultdict

def solution(id_list, report, k):
    report = set(report)
    answer = []

    mails = defaultdict(int)  # 메일 받을 개수 딕셔너리
    users = defaultdict(int)  # 유저 초기화
    for u in id_list:
        mails[u]
        users[u]

    reports = defaultdict(list)  # 신고 한 사람 저장
    for r in report:
        a, b = r.split()
        reports[b].append(a)

    for i in users:  # 신고 당한 횟수 지정 
        users[i] = len(reports[i])
        pass

    for user in users: # "신고가 k번 이상인 유저"를 신고한 사람들의 메일 받을 횟수 초기화
        if users[user] >= k:  # k보다 많이 신고 당했으면
            for c in reports[user]:
                mails[c] += 1            

    for ans in mails:
        answer.append(mails[ans])

    return answer
