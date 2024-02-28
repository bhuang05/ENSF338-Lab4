#1. The best case is O(n) and it occurs when the if-statement is not true so when all the values in the data are less than 5. This is because the code has to 
#iterate through all elements at least once due to the for loop at the start, but the second for loop which goes through everything again won't occur.
#The worst case is when all the elements in the list are greater than 5 which triggers the if statement and second for loop everytime. This has 
#a complexity of O(n^2) because the loops are going through all the values in the list twice. 
# The average case complexity is also O(n^2), assuming that a uniformly distributed list is passed through. This is because it will always go through
#all elements in the list at least one time which is O(n), but we can assume that on average around half of the list has elements that are greater than five
#leading to the second loop because activated. We can combine the cases to have a total time complexity of O(n^2/2), but due to big O notation simplifies to just O(n^2).
#Or we could just add the best and worst cases together and divide them by 2 which would give us (n^2 + n)/2 which simplifies to n^2 so it has complexity O(n^2)

#2.
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
