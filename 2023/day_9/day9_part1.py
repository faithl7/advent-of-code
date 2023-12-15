
def predict_next(seq):

    #create an empty list to store  pairwise_differences

    pd = []

    #loop through length of sequence to get pairwise_differences of the numbers in the list

    for i in range(len(seq)-1):
        pairwise_difference = seq[i+1] - seq[i]
        pd.append(pairwise_difference)

    #print(pd)    

    #pd = pairwise_difference[num]

    #check if all the numbers in pd are zero (0)
    
    test= all(i == 0 for i in pd)
    #if number is 0, add it to last number from previous sequence
    if test:
        return 0 + seq[-1]
    else:
    #if not 0, continue with pairwise_differences, with pd of sequence as input for next sequence
        return seq[-1] + predict_next(pd)
    #sum up last numbers of pd(s) to get (next) extrapolated value of history (input) sequence


#to get sum of all extrapolated values:
result = 0

#open and read input file

with open("input.txt", "r") as file:

    for line in file:
        line = [int(n) for n in line.strip().split()]

     #get sum of extrapolated values by adding up predicted_next value of every line in the file
        result += predict_next(line)

          
print(result) #sum of extrapolated values