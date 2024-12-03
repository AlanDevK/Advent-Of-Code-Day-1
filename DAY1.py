fi = open('DAY1.inp')
locIP1 = []
locIP2 = []
locList = fi.readlines()
fi.close()
for line in locList:
    newLine = line
    item1, item2 = map(int, newLine.split("   "))
    locIP1.append(item1)
    locIP2.append(item2)
locIP1.sort()
locIP2.sort()
totalDistance = 0
occuranceTimes = 0
for i in range(0, len(locIP1)):
    totalDistance += abs(locIP1[i] - locIP2[i])
    occuranceTimes += locIP1[i] * locIP2.count(locIP1[i])
fo = open('DAY1.out', 'w')
fo.write(str(totalDistance))
fo.write("\n")
fo.write(str(occuranceTimes))
fo.close()
