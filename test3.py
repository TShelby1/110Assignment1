# def numbers():
#     for n in range(1,21):
#         if n is not 11 and n is not 13:
#         if n is not in [11,13]
#             print(n)
   

def lowest():
    prices = [12,234,123,56,678,45,7,3,567,2423,56,-2,345,6752,-34,345,0,0,2]

    
    cheapest = prices[0]
    for num in prices:
        if num < cheapest:
            cheapest = num

    print(f"This is the cheapeset number: {cheapest}")  #need an f when putting values inside a string 

#numbers()
lowest()

