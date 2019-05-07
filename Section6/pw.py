# encoding:utf-8
#! python3
#pw.py -An insecure password locker program.
import sys,pyperclip
PASSWORDS={'blog':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'email':'VmALvQyKAxiVH5G8v01if1MLZF3sdt','weibo':'12345'}
if len(sys.argv)<2:
    print('Usage:python pw.py [account] copy account password.')
    sys.exit(0)

account=sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)