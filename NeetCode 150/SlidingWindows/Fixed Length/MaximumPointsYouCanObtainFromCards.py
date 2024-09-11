def maxScore(cards, k):
    total = sum(cards)
    if k >= len(cards):
        return total
    
    state = 0
    max_points = 0
    start = 0
    
    for end in range(len(cards)):
        state += cards[end]
        
        if end - start + 1 == len(cards) - k:
            max_points = max(total - state, max_points)
            state -= cards[start]
            start += 1
    return max_points

w = end - start + 1 # Tamano de la ventana
#### EXPLANATION

def maxScore(cards, k):
    # Calculate the total sum of the entire list of cards.
    total = sum(cards)
    
    # If the number of cards you can take (k) is greater than or equal to the length of the cards list,
    # you can take all the cards, so return the total sum.
    if k >= len(cards):
        return total
    
    # Initialize variables:
    state = 0          # This will represent the sum of the current window of cards (that are not part of the selection).
    max_points = 0      # Variable to store the maximum points found so far.
    start = 0           # Starting index of the sliding window.
    
    # Iterate through the cards using a sliding window approach. The 'end' pointer moves to the right,
    # representing the end of the window.
    for end in range(len(cards)):
        state += cards[end]  # Add the card at 'end' to the current window sum (state).
        
        # Once the window size reaches 'len(cards) - k' (the part of the cards we don't select),
        # we need to calculate the remaining sum, which represents the selected cards.
        if end - start + 1 == len(cards) - k:
            # Calculate the points from the cards outside the window (which is total - state).
            # Update the maximum points if this result is higher.
            max_points = max(total - state, max_points)
            
            # Shrink the window by moving 'start' to the right and subtracting 'cards[start]' from 'state'.
            state -= cards[start]
            start += 1
    
    # After sliding through the entire list, return the maximum points.
    return max_points