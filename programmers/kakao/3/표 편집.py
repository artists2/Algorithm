class Node:
    def __init__(self) -> None:
        self.removed = False
        self.next = None
        self.prev = None


def solution(n, k, cmd):
    answer = ''
    tables = [Node() for _ in range(n)]

    for i in range(1, n):  # 연결리스트 Node를 연결 시키는 작업
        tables[i-1].next = tables[i]
        tables[i].prev = tables[i-1]

    cursor = tables[k]  # 연결리스트 를 가르키는 커서 (pointer역할)
    remove_stack = []

    for c in cmd:
        c = c.split()

        if c[0] == "U":
            for _ in range(int(c[1])):  # c[1] 만큼 cursor 이동 (UP)
                cursor = cursor.prev
        elif c[0] == "D":
            for _ in range(int(c[1])):  # c[1] 만큼 cursor 이동 (DOWN)
                cursor = cursor.next
        elif c[0] == "C":  # 삭제 -> 다시연결
            remove_stack.append(cursor)
            cursor.removed = True
            if cursor.prev:
                cursor.prev.next = cursor.next
            if cursor.next:
                cursor.next.prev = cursor.prev
                cursor = cursor.next
            else:  # cursor.next가 없는 경우(마지막 행인 경우)
                cursor = cursor.prev

        else:  # c[0] == "Z"  노드를 pop으로 꺼내서 연결해주는 작업
            node = remove_stack.pop()
            node.removed = False
            if node.prev:
                node.prev.next = node
            if node.next:
                node.next.prev = node
    for i in range(n):
        if tables[i].removed:
            answer += "X"
        else:
            answer += "O"


    return answer

# def solution(n, k, cmd):
#     answer = ''
#     tables = [i for i in range(n)]
#     remove_stack = []
#     pointer = k
#     for c in cmd:
#         c = c.split() 
#         if c[0] == "U":
#             u, i = c[0], int(c[1])
#             pointer -= i
#         elif c[0] == "D":
#             d, i = c[0], int(c[1])
#             pointer += i
#         elif c[0] == "C":
#             remove_stack.append((pointer, tables[pointer]))
#             del tables[pointer]
#             if pointer == len(tables):
#                 pointer -= 1
#         else:
#             v = tables[pointer]
#             p, e  = remove_stack.pop()
#             tables.insert(p, e)
#             pointer = tables.index(v)

#     for i in range(n):
#         if i in tables:
#             answer += "O"
#         else:
#             answer += "X"
#     return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))