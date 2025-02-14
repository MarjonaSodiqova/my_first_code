from collections import Counter

def uncommon_elements(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    result = []   
    for element in counter1:
        if element not in counter2:
            result.extend([element] * counter1[element])
        elif counter1[element] != counter2[element]:
            result.extend([element] * abs(counter1[element] - counter2[element]))
    
    for element in counter2:
        if element not in counter1:
            result.extend([element] * counter2[element])
        elif counter2[element] != counter1[element]:
            result.extend([element] * abs(counter2[element] - counter1[element]))
    
    return result
list1_input = input("LIST1(you should write comma between numbers)= ").split(',')
list2_input = input("LIST2(you should write comma between numbers)= ").split(',')
list1 = [int(i) for i in list1_input]
list2 = [int(i) for i in list2_input]
uncommon = uncommon_elements(list1, list2)
print("Uncommon elements:", uncommon)
