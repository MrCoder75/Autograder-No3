### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def hcf(ali_budget,bashir_budget):

    if ali_budget > bashir_budget:
        smaller = bashir_budget
    else:
        smaller = ali_budget
    for i in range(1, smaller+1):
        if((ali_budget % i == 0) and (bashir_budget % i == 0)):
            hcf = i 
    return hcf
   
def chocolatePrice(ali_budget,bashir_budget):
    return hcf(ali_budget,bashir_budget)

#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget,bashir_budget):
    if type (ali_budget) == float or type(bashir_budget)==float:
        return bb(ali_budget,bashir_budget)
    else:
        return("Not Possible")
    
def bb(ali_budget,bashir_budget):
    if ali_budget > bashir_budget:
        ali_profit= ali_budget*1.5
        bashir_profit= bashir_budget*2
        return bashir_profit-bashir_budget
    else:
        bashir_profit= bashir_budget*1.5
        ali_profit= ali_budget*2
        return ali_profit-ali_budget

#### End OF MARKER


