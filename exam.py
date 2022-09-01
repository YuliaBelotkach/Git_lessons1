def kartochka(card):
    return '*' * len(card[:-4]) + card[-4:]

print(kartochka('1626575781724356'))

def palindrome(str):
    str = str.replace(' ', '').lower()
    return 'Палиндром' if str == str[::-1] else 'Не палиндром'

print(palindrome('lllfhhhdhhf'))
print(palindrome('vnnvnvnnvnv'))
print(palindrome('12233221'))