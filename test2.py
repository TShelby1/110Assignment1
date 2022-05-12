### Lists

from mock_data import mock_catalog


def test_1():
    print("basic python lists")


    nums =[1,2,3,4,5,6,7,8,9,23,34,455,]


    # to read the numbers
    print(nums[0])
    print(nums[3])

    #add the numbers
    nums.append(42)
    nums.append(-1)

    #remove by element, not for objects, its for simple stuff
    nums.remove(23)


    #we like to use remove by index, it remoes the item by position, below removes first item in list
    del nums[0]



    print(nums)


    #loop
    for n in nums:
        print(n)

def test_2():
    print("Some numbers")

    prices = [12.23,345,123.2,542,65,123.2,0.223,-23,123.2,6,171,5678]

    #sum
    total = 0
    cheapest = prices[0]
    for num in prices:
        total+= num
    
        if num < cheapest:
            cheapest = num
        
    print(total)
    print(f"The cheapest price is: {cheapest}")

    
def test_3():
    print("cheapest product")
        
    
# for loop to print every dict/prodcut from the mock_catalog
#print only the title of every product
    solution = mock_catalog[0]

    for prod in mock_catalog:
        if prod["price"] < solution["price"]:
            solution = prod


    print(f"The cheapest product is: {solution['title']} - ${solution['price']}")
    #the cheapest product is: Title - Price



# call
#test_1()
#test_2()
test_3()