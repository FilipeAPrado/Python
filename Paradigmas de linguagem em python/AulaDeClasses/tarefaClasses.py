from account import Account

account1 =Account(input('inform the account number: '))
account2 = Account(2)




print('Welcome to acount')
action = input('want to insert credit into your account? ? [s] or [n] ')
credit = account1.credit(int(input('how much do you want to credit: '))) if action == 's' else print('ok')

action = input('want to check your account balance? [s] or [n] ')
chekcBalance = account1.checkBalance() if action == 's' else 'ok'
print(chekcBalance)

action = input('want to transfer money from the account? [s] or [n]') 
transferValue = input('what amount do you want to transfer: ') if action == 's' else 'ok'
transferValue = int(transferValue) if transferValue != 'ok' else 'ok'
transfer = account1.transfer(account2,transferValue) if transferValue != 'ok' else 'ok'
print(f'your current balance is:{account2.checkBalance()}')