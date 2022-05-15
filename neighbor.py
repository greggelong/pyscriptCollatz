def collatzNeighbors(num):
    ''' get the collatz neighbors of a number
        return as a immutable tuple'''
    if num%2 ==0:
        # form 3np1 factor
        if (num-1)%3 == 0:       
            #print(num, (num-1)/3, "or", num*2, "or" ,num/2 )
            return ((num-1)/3, num*2, num/2)
        else:
        # not 3np1 factor
            #print(num, "not 3np1", num*2 , "or",num/2)
            return (num*2, num/2)
    else:
        # cant divide by two as its odd so 3np1 and mult by 2
        #print( num, "is odd so 3np1" , num*3+1, "or", num*2)
        return (num*3+1, num*2)
        