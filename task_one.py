user_year=input('Please enter your year of birth:')
year=int(user_year)
current_year=2018
age=current_year-year
if age<18:
    print('You are a minor.')
elif age>36:
    print('You are an elder.')
else:
    print('You are a youth.')
