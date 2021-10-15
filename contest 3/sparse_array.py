
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    # strings = list(set(strings))
    print(strings, " is strings")
    for q in queries:
        count = 0
        for i in strings:
            if q == i:
                count += 1 
            
        result.append(count)
        
    return result