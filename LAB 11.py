'''1. Create a code that will ask for your marketing budget.
 Facebook campaign = 100ILS per day.
 Instagram campaign = 50ILS per day.
Ask him:
How long he wants the Facebook campaign will run.
How long he wants the Instagram campaign will run.
Then print to the screen the summary of the cost in ILS with tax (17%)
If it is more than his marketing budget, tell him how much to add, if not tell him "successful".
'''

print('''MENU:
Facebook campaign = 100ILS per day.
Instagram campaign = 50ILS per day.
''')
budget = int(input('how much is your budget?:\n'))
facebook_run = int(input('How long do you want Facebook campaign will run.?\n'))
instagram_run = int(input('How long do you want Instagram campaign will run.?\n'))
summary_facebook = (facebook_run *100) * 1.17
summary_instagram = (instagram_run*50) *1.17
print(str(summary_facebook)+'$ for Facebook campaign')
print(str(summary_instagram)+'$ for Instagram campaign')
if summary_instagram+summary_facebook > budget:
    print(f'you don`t have enough money you will need to add {(summary_instagram+summary_facebook) - budget}$')
else:
    print('successful')


