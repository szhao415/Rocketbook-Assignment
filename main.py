import numpy as np


def answerQuestion1():
    orderTypes = np.genfromtxt('ordersSyncs.csv', dtype=str, delimiter=',', usecols=(14), skip_header=1)
    orderAmounts = np.genfromtxt('ordersSyncs.csv', dtype='f8', delimiter=',', usecols=(4), skip_header=1, filling_values = 0)
    order = np.genfromtxt('ordersSyncs.csv', dtype='f8, U40', delimiter=',', usecols=(4,14), skip_header=1, filling_values=(0, ''))
    typeDict = {}
    # for i in orderTypes:
    #     if i in typeDict:
    #         typeDict[i] += 1
    #     else:
    #         typeDict[i] = 1
    typeDictB = {}
    length = np.shape(orderTypes)[0]
    for row in order:
        if row[1] in typeDictB:
            typeDictB[row[1]] += row[0]
        else:
            typeDictB[row[1]] = row[0]
    print(np.sum(orderAmounts))
    print(typeDictB)

def answerQuestion2():
    order = np.genfromtxt('ordersSyncs.csv', dtype='U40, f8', delimiter=',', usecols=(3, 4), skip_header=1, filling_values=('', 0))
    yesPlot = np.empty(0)
    noPlot = np.empty(0)
    # for row in order:
    #     if row[0] == 'yes':
    #         yesPlot = np.append(yesPlot, row[1])
    #     elif row[0] == 'no':
    #         noPlot = np.append(noPlot, row[1])
    # index = 0
    # yesCounter = 0
    # for row in order:
    #     if row[0] == 'yes':
    #         yesCounter+= 1
    #     if yesCounter == 3355:
    #         print(index)
    #     index += 1
    # print('For Yes Plot:', np.median(yesPlot), np.mean(yesPlot), np.std(yesPlot))
    # print('For No Plot:', np.median(noPlot), np.mean(noPlot), np.std(noPlot))

    # yesPlot = np.atleast_2d(yesPlot).T
    # noPlot = np.atleast_2d(noPlot).T
    # # print(yesPlot)
    # plots = np.concatenate((yesPlot, noPlot), axis=1)
    # print(plots)
    # np.savetxt('yes.csv', yesPlot)
    # np.savetxt('no.csv', noPlot)
    order2 = np.genfromtxt('ordersSyncs.csv', dtype='U40, f8, f8, int, U40', delimiter=',', usecols=(3, 4, 5, 6, 7), skip_header=1,
                         filling_values=('', 0, 0, 0, 0))
    yesPlot2 = np.empty(0)
    noPlot2 = np.empty(0)
    for row in order2:
        index = 0
        entry = np.empty(0)
        for element in row:
            if index != 0 and index != 4:
                entry = np.append(entry, element)
            index += 1
        if row[0] == 'yes':
            yesPlot2 = np.append(yesPlot2, entry)
        elif row[0] == 'no':
            noPlot2 = np.append(noPlot2, entry)
    yesPlot2 = np.reshape(yesPlot2, (4149, 3))
    # yesPlot2 = np.delete(yesPlot2, -1, 1)
    noPlot2 = np.reshape(noPlot2, (741, 3))
    print(np.average(yesPlot2, axis=0))
    print(np.average(noPlot2, axis=0))
    yesIndex = 0
    noIndex = 0
    print(yesPlot2)
    print(noPlot2)
    for row in yesPlot2:
        if row[1] != 0:
            yesIndex += 1
    for row in noPlot2:
        if row[1] != 0:
            noIndex += 1
    print('yesIndex is', yesIndex)
    print('noIndex is', noIndex)
    # noPlot2 = np.delete(noPlot2, -1, 1)
    # np.savetxt('yesUpgraded.csv', yesPlot2)
    # np.savetxt('noUpgraded.csv', noPlot2)

def createOrders():
    yesNo = np.genfromtxt('ordersSyncs.csv', dtype=str, delimiter=',', usecols=(3), skip_header=1)
    moneys = np.genfromtxt('ordersSyncs.csv', dtype=float, delimiter=',', usecols=(5, 6, 8), skip_header=1)
    yesPrices = np.empty(0)
    noPrices = np.empty(0)
    index = 0
    for boo in yesNo:
        if boo == 'yes':
            price = (moneys[index][1]) * (moneys[index][2]) - moneys[index][0]
            if price >= 0:
                yesPrices = np.append(yesPrices, price)
            else:
                yesPrices = np.append(yesPrices, 0)
        elif boo == 'no':
            price = (moneys[index][1]) * (moneys[index][2]) - moneys[index][0]
            if price >= 0:
                noPrices = np.append(noPrices, price)
            else:
                noPrices = np.append(noPrices, 0)
        index += 1
    print('yesPrices are', np.average(yesPrices), np.median(yesPrices), np.std(yesPrices))
    print('noPrices are', np.average(noPrices), np.median(noPrices), np.std(noPrices))
    np.savetxt('yesPricesv3.csv', yesPrices)
    np.savetxt('noPricesv3.csv', noPrices)

def answerQuestion3():
    #create array of valid IDs that ordered
    orderIDs = np.genfromtxt('bugTesterRBv1.csv', dtype=str, delimiter=',', usecols=0, skip_header=1)
    transactionPrices = np.genfromtxt('bugTesterRBv1.csv', dtype=float, delimiter=',', usecols=4, skip_header=1, \
                                      filling_values=-1)
    index = 0
    newOrderIDs = np.empty(0)
    for price in transactionPrices:
        if price != -1:
            newOrderIDs = np.append(newOrderIDs, orderIDs[index])
        index += 1
    #create array of orderValues
    priceCans = np.genfromtxt('bugTesterRBv1.csv', dtype=float, delimiter=',', usecols=(5, 6, 8), skip_header=1, \
                              filling_values=-1)
    newOrderValues = np.empty(0)
    for row in priceCans:
        if row[0] != -1:
            price = (row[2] * row[1]) - row[0]
            if price < 0:
                price = 0
            newOrderValues = np.append(newOrderValues, price)
    professions = {}
    IDandProfessions = np.genfromtxt('Synced Scans.csv', dtype=str, delimiter=',', usecols=(0, 9), skip_header=1)
    origIndex = 0
    numberofEntries = 0
    for ID in newOrderIDs:
        creationIndex = 0
        if ID in IDandProfessions[:,0]:
            numberofEntries += 1
            for right in IDandProfessions[:,0]:
                if right == ID:
                    break
                creationIndex += 1
            # print('index is:', creationIndex)
            # print('ID is', ID)
            profession = IDandProfessions[creationIndex, 1]
            if profession not in professions:
                professions[profession] = np.empty(0)
            professions[profession] = np.append(professions[profession], newOrderValues[origIndex])
        origIndex += 1
    for jobs in professions:
        print(jobs, 'total revenue is:', np.sum(professions[jobs]),'; average order value is', np.average(professions[jobs]))
    print('number of entries is', numberofEntries)
    print('professions dictionary is:', professions)
def propertySearch(columnIndex):
    # create array of valid IDs that ordered
    orderIDs = np.genfromtxt('bugTesterRBv1.csv', dtype=str, delimiter=',', usecols=0, skip_header=1)
    transactionPrices = np.genfromtxt('bugTesterRBv1.csv', dtype=float, delimiter=',', usecols=4, skip_header=1, \
                                      filling_values=-1)
    index = 0
    newOrderIDs = np.empty(0)
    for price in transactionPrices:
        if price != -1:
            newOrderIDs = np.append(newOrderIDs, orderIDs[index])
        index += 1
    # create array of orderValues
    priceCans = np.genfromtxt('bugTesterRBv1.csv', dtype=float, delimiter=',', usecols=(5, 6, 8), skip_header=1, \
                              filling_values=-1)
    newOrderValues = np.empty(0)
    for row in priceCans:
        if row[0] != -1:
            price = (row[2] * row[1]) - row[0]
            if price < 0:
                price = 0
            newOrderValues = np.append(newOrderValues, price)

    creationIndex = 0
    professions = {}
    IDandProfessions = np.genfromtxt('Synced Scans.csv', dtype=str, delimiter=',', usecols=(0, columnIndex), skip_header=1)
    origIndex = 0
    for ID in newOrderIDs:
        creationIndex = 0
        if ID in IDandProfessions[:,0]:
            for right in IDandProfessions[:,0]:
                if right == ID:
                    break
                creationIndex += 1
            # print('index is:', creationIndex)
            # print('ID is', ID)
            profession = IDandProfessions[creationIndex, 1]
            print(profession, ID, newOrderValues[origIndex])
            if profession not in professions:
                professions[profession] = np.empty(0)
            professions[profession] = np.append(professions[profession], newOrderValues[origIndex])
        origIndex += 1
    total = 0
    smrevenue = 0
    smcount = 0
    applecount = 0
    applerevenue=0
    otherCount = 0
    otherrevenue = 0
    for jobs in professions:
        if jobs[0] == 'i':
            applerevenue += np.sum(professions[jobs])
            applecount += np.size(professions[jobs])
        elif 'SM' in jobs:
            smrevenue += np.sum(professions[jobs])
            smcount += (np.size(professions[jobs]))
        else:
            otherrevenue += (np.sum(professions[jobs]))
            otherCount += (np.size(professions[jobs]))
        print(jobs, 'total revenue is:', np.sum(professions[jobs]), '; average order value is',
              np.average(professions[jobs]))
        total += np.sum(professions[jobs])
    print('absolute total revenue is:', total)
    print('professions dictionary is:', professions)
    if smrevenue != 0:
        print('Samsung revenue and count is ', smrevenue, smcount)
        print('apple revenue and count is', applerevenue, applecount)
        print('other revenue and count is', otherrevenue, otherCount)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # answerQuestion1()
    # answerQuestion2()
    createOrders()
    # answerQuestion3()
    # propertySearch(3)
    # propertySearch(4)
    # propertySearch(7)
    # propertySearch(11)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
