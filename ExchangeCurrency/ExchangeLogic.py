print('Which currency pair do you want to convert?')
print('---------------------------')
print('1. USD -> VND')
print('2. VND -> USD')
print('---------------------------')

UserChoice = input()
Choice = int(UserChoice)
print('You choose: ' + UserChoice)
if (Choice == 1):
    print('Enter USD: ')
    UserInput = input()
    usd = int(UserInput)
    vnd = usd * 23
    #print(str(UserInput) + " USD = "+ str(vnd) + " VND") #Or may use this way
    print('%s USD = %d.000 VND' %(usd, vnd))
elif (Choice == 2):
    print('Enter VND: ')
    UserInput = input()
    vnd = int(UserInput)
    usd = vnd/23
    #print(str(UserInput) + "VND = "+ str(usd) + "USD")
    print('%d VND = %.5f USD' %(vnd, usd))
else:
    print('Invalid choice!')

# switch(Choice)
# {
#     case (1):
#         print('Enter USD: ')
#         UserInput = input();
#         vnd = UserInput * 23;
#         print(str(UserInput) + "USD = "+ str(vnd) + "VND");
#         break;
#     case (2):
#         print('Enter VND: ')
#         UserInput = input()
#         usd = UserInput / 23
#         print(str(UserInput) + "VND = "+ str(usd) + "USD")
#         break;
#     default:
#         print('Invalid choice!')
#         break;
# }
