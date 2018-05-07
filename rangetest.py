'''
for i in range(2,13,4):
    print(i)
'''
names = ["Alex","John","Mary","Steve","John", "Steve"]

def check_value():
    i = 0
    v = 1
    while names[i] < len(names):
        names[i] += 1
        names[v] += 1
        if names[i] == names[v]:
            print("Same name")
        elif names[1] != names[3]:
            print("Not same name")
        elif names[1] == names[4]:
            print("Bingo!")
check_value()