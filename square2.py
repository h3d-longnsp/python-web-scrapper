# Define a function to be executed in parallel
def square(numbers):
    results = []
    for number in numbers:
        results.append(number ** 2)
    return results


numbers = [1456345645645645654, 45645645645646452, 4564564564563, 4, 5]

results = list(map(square, [numbers]))

# Print the results
print(results)