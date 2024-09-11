def fruit_into_baskets(fruits):
    start = 0
    state = {}
    max_fruit = 0
    
    for end in range(len(fruits)):
        # tomamos el indice de la fruta en el
        # diccionario y adicionamos 1
        state[fruits[end]] = state.get(fruits[end], 0) + 1

        while len(state) > 2:
            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            state += 1
        max_fruit = max(max_fruit, end - start + 1) 
        
    return max_fruit
