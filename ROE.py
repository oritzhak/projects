

check = True
while check:
    money_first_invest = input( 'please enter amount of the money that you invested:\nenter numbers only!!!\n')
    net_money= input('please enter the current money:\nenter numbers only!!!\n')

    if money_first_invest.isnumeric() and net_money.isnumeric():
        check = False

profit = int(net_money) - int(money_first_invest)

result_precent = (int(profit) / int(money_first_invest)) * 100

print('you made ROE of: ' + str('%.2f' % result_precent) + '%')

