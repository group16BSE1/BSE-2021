def chop(list):
    firstChop = list[1:]
    lengthOfChop = len(firstChop)
    none = firstChop[:lengthOfChop-1]
    print(none)
    return none


def middle(mlist):
    newlist = mlist[1]
    NoOfListItems = len(newlist)
    new = newlist[:NoOfListItems-1]
    print(new)
    return new


fruit = ['Mango', 'Orange', 'Pineapple', 'Peach']
print(fruit)

x = chop(fruit)
y = middle(fruit)

if x == y:
    print('Its identical and equivalent!')
else:
    print('Its not identical and equivalent')