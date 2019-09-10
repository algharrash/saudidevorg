#Python Dictionary part 1

myInfo = {
    'Name' : 'Ali',
    'Nationality' : 'Saudi',
    'twitter' : 'algharrash',
    'Hoppy' : 'Reading'
}

print(myInfo)

myInfo['twitter'] = '@algharrash'
for x, y in myInfo.items():
    print(x + ' : ' + y)

