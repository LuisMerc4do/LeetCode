def dailyTemperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result


#EXPLANATION
def dailyTemperatures(temps):
  n = len(temps)  # Get the number of days (or length of the temps list)
  result = [0] * n  # Initialize the result list with zeros, same length as temps
  stack = []  # Stack to store indices of temperatures we haven't found warmer days for yet
  for i in range(n):
    while stack and temps[i] > temps[stack[-1]]:
      idx = stack.pop()  # Get the index of the day we are checking
      result[idx] = i - idx  # Calculate how many days we had to wait for a warmer day
    stack.append(i)  # Add the current day to the stack
  return result  # Return the result list with the number of days to wait for a warmer day
