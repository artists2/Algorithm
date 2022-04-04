































































# from collections import defaultdict
# from itertools import combinations

# def solution(sentences, n):


#     answer = -1
    
#     for sent in sentences:
#         score = 0
#         count = 0
#         flag = 0
#         tmp = []
#         for s in set(sent):
#             if count > n:
#                 break
#             if s.isupper():
#                 score += 1
#                 flag = 1
#             if s == " ":
#                 continue
            
#             tmp.append(s.lower())
        
#         if count > n:
#             continue
#         else:
#             if flag:
#                 count += 1  # shift
#                 flag = 0
#                 tmp.append("shift")

#             count += len(set(sent))
#             if " " in sent:
#                 count -= 1
#                 # print("count : ", sent.count(" "))
#             score += len(sent)
            
#             print("score: ", score, "count: ", count)
#             tmp.append((score, count))
#             print(tmp)


#     return answer

# print(solution(["line in line", "LINE", "in lion"], 5))
# print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))




























# import sys

# def solution(logs):
#     answer = -1
#     flag = 0
#     count = 0
#     for log in logs:
#         if len(log) > 100:
#             continue
#         if len(log.split(" ")) != 12:
#             continue
#         strr = []
#         for strings in log.split(" "):
#             print(strings)
#             if strings == ":":
#                 continue
#             if strings == "team_name":
#                 flag = 1
#                 continue
#             if strings == "application_name":
#                 flag = 1
#                 continue
#             if strings == "error_level":
#                 flag = 1
#                 continue
#             if strings == "message":
#                 flag = 1
#                 continue
            
#             if flag:
#                 if strings.isalpha():
#                     flag = 0
#                     strr.append(strings)
#                 else:
#                     continue
#         if len(strr) == 4:
#             count += 1
#     return len(logs) - count

# print(solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]))

# print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))





# # answer = -1
# #     count = 0
# #     flag = 0
# #     tmp_lst = ["team_name", "application_name", "error_level", "message"]
# #     print(len(logs))
# #     for l in logs:
# #         ok_log = []
# #         print(l)
# #         if len(l) > 100:
# #             continue
        
# #         else:
# #             for s in l.split(' '):
# #                 a = s.split(' ')
# #                 print(s)
# #                 if s == ":":
# #                     continue
# #                 if s == "team_name":
# #                     flag = 1
# #                     ok_log.append(s)
# #                     continue
# #                 if s == "application_name":
# #                     flag = 1
# #                     ok_log.append(s)
# #                     continue
# #                 if s == "error_level":
# #                     flag = 1
# #                     ok_log.append(s)
# #                     continue
# #                 if s == "message":
# #                     flag = 1
# #                     ok_log.append(s)
# #                     continue
                
# #                 if flag:
# #                     if s.isalpha():
# #                         flag = 0
# #                     else:
# #                         continue
# #                 else:
# #                     continue
# #             if tmp_lst == ok_log:
# #                 count += 1
# #                 print(l)
# #     answer = len(logs) - count