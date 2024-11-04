class Item:
    def __init__(self, value, weight):  # Corrected __init__ method
        self.value = value
        self.weight = weight

def fractionalKnapsack(W, arr):
    # Sorting Items based on value-to-weight ratio
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    finalvalue = 0.0  # Variable to store the total value in the knapsack

    # Loop through all items
    for item in arr:
        # If adding the item won't exceed capacity, add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        # If we can't add the whole item, add the fractional part of it
        else:
            finalvalue += item.value * (W / item.weight)
            break

    return finalvalue  # Return the maximum value of knapsack

# Driver Code
if __name__ == "__main__":  # Corrected condition for main block
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    
    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(f"Maximum value in Knapsack = {max_val}")
