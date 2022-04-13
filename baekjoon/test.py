

def create_command(time, meter, turn):
    command_string = f"Time {time}: Go straight {meter}m and turn {turn}"

    return command_string

def check_directions(check, p):
    result = ""
    if check == "E":
        if p == "N":
            return "left"
        if p == "S":
            return "right"

    if check == "N":
        if p == "W":
            return "left"
        if p == "E":
            return "right"

    if check == "W":
        if p == "S":
            return "left"
        if p == "N":
            return "right"

    if check == "S":
        if p == "E":
            return "left"
        if p == "W":
            return "right"


def solution(path):
    answer = []
    stck = []
    check = path[0]
    time = 0
    while time != len(path):
        if path[time] != check:
            # print(stck)
            if len(stck) < 5:
                meter = len(stck) * 100
                d = check_directions(check, path[time])

                if not answer:
                    # print(create_command(0, meter, d))
                    answer.append(create_command(0, meter, d))
                else:
                    # print(create_command(time - len(stck), meter, d))
                    answer.append(create_command(time-len(stck), meter, d))

            else:
                # print(time, stck)
                meter = 500
                d = check_directions(check, path[time])
                # print(create_command(time - len(stck) + 1, meter, d))
                answer.append(create_command(time - 5, meter, d))

            stck.clear()
            check = path[time]

        stck.append(path[time])
        time += 1


    return answer

print(solution("EEESEEEEEENNNN"))
# print(solution("SSSSSSWWWNNNNNN"))