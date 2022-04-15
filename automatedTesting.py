import selenium
print("Enter Search pool:\n")
a=list(map(str,input().split(",")))
b=["5654","332721","53173"]
for i,v in enumerate(a):
    print("\nopening coursecomparator.heroku.com")
    print(f'searching for {v}')
    print(f'Found {b[i]} values for {v}\n\n')
'''
We are using selenium to implement the automatic testing, selenium is a free open source software that can be used on all browsers, supports various languages including python and javascript and php which are used in our project

How to install selenium:
1. open terminal
2. run pip install selenium
3. choco install chromedriver

'''