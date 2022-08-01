print('Welcome to the love calculator!')

name1 = input('What is your name? ')
name2 = input('What is your partner\'s name? ')

combined_names = name1 + name2
lowercasing_names = combined_names.lower()

t = lowercasing_names.count('t')
r = lowercasing_names.count('r')
u = lowercasing_names.count('u')
e = lowercasing_names.count('e')

true = t + r + u + e

l = lowercasing_names.count('l')
o = lowercasing_names.count('o')
v = lowercasing_names.count('v')
e = lowercasing_names.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}, Una two no too gel')
elif love_score >= 40 and love_score <= 50:
    print(f'Your love score is {love_score}, You are a good match')

else:
    print(f'Your love score is {love_score}')

