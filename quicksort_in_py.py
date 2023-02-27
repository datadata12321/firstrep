import time

def quick_sorting(listing, leftside, rightside):
    if leftside >= rightside:
        return
    
    ri = rightside
    le = leftside

    while(le < ri):

        le = le + 1 # listing[leftside] is pivot element
        
        while(le < rightside and listing[le] <= listing[leftside]):
            le = le + 1

        while(ri > leftside and listing[ri] >= listing[leftside]):
            ri = ri - 1
        
        # then listing[le] > listing[leftside], listing[ri] < listing[leftside] 
        # which means they have to be in each other's place --- exchanged

        if (le < ri):
            tmp = listing[le] 
            listing[le] = listing[ri]
            listing[ri] = tmp
    
    # after while(le < ri) is done, then le > ri or le = ri --- listing[ri] < listing[leftside] 
    # 2 "while" syntaxes in outer "while" syntax may decide whether "le=ri" can happen? 
    # "partition function" is done by "while" --- our pivot goes into listing[ri]
    # "ri" is our new pivot

    tempo = listing[ri]
    listing[ri] = listing[leftside]
    listing[leftside] = tempo

    quick_sorting(listing, leftside, ri - 1)
    quick_sorting(listing, ri + 1, rightside)

listing_2 = [0.5, 0.3, 1, 5, 47, 3, 5, 2, 14, 14, 17, 170, 2800, 1770]
s = time.time()
quick_sorting(listing_2, 0, len(listing_2)-1)
f = time.time()
print(f-s) # need larger data to scale time complexity......
print(listing_2)       