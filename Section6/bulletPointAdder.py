# encoding:utf-8
#! python3
# bulletPointAdder.py Adds wikipedia bullet points to start 
# of each line of text on the clipboard.
import pyperclip,sys
text = pyperclip.paste()
if text==None or type(text)!=str:
    print("Clipboard has not string content!")
    sys.exit(0)
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
print('Process OK!')