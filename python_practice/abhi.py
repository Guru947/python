# # spam=[[1,2],[3,4],['rat','cat']]
# # print(len(spam))
# #
# # import random
# # message=['it is certain','yes','good day']
# # print(message.index([random.randint(0,len(message)-1)]))
# # name="BRo"
# # def disply_name():
# #
# #     global name
# #     name = "code"
# #     print(name)
# # disply_name()
# # print(name)
#
# # limited number of guesses
# def numguess():
#     n=18
#     i=6
#     print("Total number of guesses are 6")
#     while(i>=0):
#         c=int(input("Enter the number"))
#         if c>18:
#             print("Your guessed number is greater__guesses lower")
#         elif c < 18:
#             print("Your number is lesses __guesses greater")
#         else:
#             print("you entered correct number!!!@@@ ")
#             print("Number of chances took to complete is",6-int(i))
#             break
#         print("number of guesses left --",i)
#         i-=1
#         if i==0:
#             print("Your chances are over!")
#             print("GAME OVER")
#             break
#     numguess()
#
#
#     print("press YES /NO to continue or exit")
#     ch=input("Enter YES/NO").upper()
#     if ch == "YES":
#         print('gf')
#     else:
#         print("THanks for playing")
#
#
#
#
#
#
#
# import copy
# spam=[8,9,10,11]
# cheese = copy.copy(spam)
# cheese[3]=55
# print(spam)
# print(cheese)

# var=10
# if var==100:
#     print("value of")
# else:

# def palindrome(strings):
#     print("your input is :", strings)
#     b = strings[::-1]
#     print("The reverse of the string is :",b)
#     if strings == b:
#         print(f"The {strings}  is == {b} so it is palindrome")
#     else:
#         print(f"{strings} != {b} so its not palindrome")
# st=input("Enter the string to check")
# palindrome(st)
