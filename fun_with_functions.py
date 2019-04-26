def odd_even():
    for num in range(1, 2001):
        if num % 2 == 0:
            print "Number is ", num,". This is an even number." 
        else:
            print "Number is ", num,". This is an odd number."

# odd_even()

nums = [2,3,10,16]

def multiply(input, mult):
    products = []
    for num in input:
        pro = mult * num
        products.append(pro)
    return products

print multiply(nums, 5)

def layered_mults(arr):
    outer_arr = []
    
    for num in arr:
        inner_arr = []
        nam = 0

        for ele in range(1, num + 1):
            nam += 1
            inner_arr.append(nam)

        outer_arr.append(inner_arr)

    return outer_arr

print layered_mults(multiply(nums, 5))

