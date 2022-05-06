def solution(numbers, hand):
    answer = ''
    keypad_location = {
        1 : (0, 0),
        2 : (0, 1),
        3 : (0, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (2, 0),
        8 : (2, 1),
        9 : (2, 2),
        '*': (3, 0),
        0 : (3, 1),
        '#': (3, 2)
    }
    l = [1, 4, 7]
    r = [3, 6, 9]
    left_point = keypad_location['*']
    right_point = keypad_location['#']

    for key in numbers:
        if key in l:
            answer += 'L'
            left_point = keypad_location[key]
        elif key in r:
            answer += 'R'
            right_point = keypad_location[key]
        else:
            left_count = abs(keypad_location[key][0] - left_point[0]) + abs(keypad_location[key][1] - left_point[1])
            right_count = abs(keypad_location[key][0] - right_point[0]) + abs(keypad_location[key][1] - right_point[1])
            #print(key, left_count, right_count)
            if left_count < right_count:
                answer += 'L'
                left_point = keypad_location[key]
            elif left_count > right_count:
                answer += 'R'
                right_point = keypad_location[key]
            else: # ==
                if hand == 'right':
                    answer += 'R'
                    right_point = keypad_location[key]
                if hand == 'left':
                    answer += 'L'
                    left_point = keypad_location[key]



    return answer




print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"
print(solution([7, 0], 'left'))