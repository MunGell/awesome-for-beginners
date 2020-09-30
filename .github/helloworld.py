name = input('what is your good name?')
age =  int(input('what is your age {0}'.format(name)))
if age>=18:
    print('{0} you are eligible to vote'.format(name))
else:
    print('you are not eligible to vote. please come after {0} years'.format(18-age))