print("Inside file process")
import string
import re
remove = string.punctuation
for ch in ['.',',','-']:
        remove = remove.replace(ch, "") #dont remove . and , 
pattern = r"[{}]".format(remove)
def clean(x):

    x = x.encode('ascii', 'ignore').decode()
    x = re.sub(r'https*\S+', '', x) #https
    x = re.sub(r'@\S+', '', x) #@
    x = re.sub(r'#\S+', '', x)# #
    x = re.sub(r'\'\w+', '', x)#  Remove ticks and the next character
    #x = re.sub(r'\w*\d+\w*', '', x)  to remove numbers 
    x = re.sub(r'[\(\{\[].*?[\}\)\]]', ' ', x) # Remove strings inside {} [] ()
    x = x.translate(str.maketrans('', '',pattern))
    x = re.sub(r' - ','',x) # remove unneccessary hyphens
    x = re.sub(r'\s{2,}', ' ', x)# Replace the over spaces
    return x

#text=clean(text)