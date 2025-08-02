class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        map1 = {}
        map2 = {}
        global_min = float("inf")
        for price in basket1:
            global_min = min(global_min, price)
            if price not in map1:
                map1[price] = 0
            if price not in map2:
                map2[price] = 0
            map1[price] += 1

        for price in basket2:
            global_min = min(global_min, price)
            if price not in map1:
                map1[price] = 0
            if price not in map2:
                map2[price] = 0
            map2[price] += 1

        array1 = []
        array2 = []
        count1 = 0
        count2 = 0
        for uniq_prices in map1.keys():
            if map1[uniq_prices] == map2[uniq_prices]:
                map1[uniq_prices] = 0 
                map2[uniq_prices] = 0
                continue
            elif map1[uniq_prices] > map2[uniq_prices]:
                diff = map1[uniq_prices] - map2[uniq_prices]
                if diff % 2 == 0:
                    count1 += diff // 2
                    map1[uniq_prices] = diff // 2
                    map2[uniq_prices] = 0
                    array1.append(uniq_prices)
                else :
                    return -1
            else :
                diff = map2[uniq_prices] - map1[uniq_prices]
                if diff % 2 == 0:
                    count2 += diff // 2
                    map2[uniq_prices] = diff // 2
                    map1[uniq_prices] = 0
                    array2.append(uniq_prices)
                else :
                    return -1
            
        if count1 != count2:
            return -1
        array1.sort()
        array2.sort()
        # print("map1 --> ",map1)
        # print("array1 --> ",array1)

        # print("map2 --> ",map2)
        # print("array2 --> ",array2)
        i = 0 # array 1 starting pointer
        min_cost = 0
        while len(array2):
            mini = array1[i]
            maxi = array2[-1]

            if map1[mini] > map2[maxi]:
                map1[mini] -= map2[maxi]
                min_cost += min(min(mini, maxi) * map2[maxi], 2* global_min *map2[maxi] )
                map2[maxi] = 0
                array2.pop()
            else :
                map2[maxi] -= map1[mini]
                if map2[maxi] == 0:
                    array2.pop()
                min_cost += min(min(mini, maxi) * map1[mini], global_min * 2 * map1[mini])
                map1[mini] = 0
                i += 1
            print(min_cost)
        return min_cost
            




            

                
        