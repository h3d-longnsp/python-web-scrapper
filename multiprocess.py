import multiprocessing

# Define a function to be executed in parallel
def square(numbers):
    results = []
    for number in numbers:
        results.append(number ** 2)
    return results

# Define the input data to be processed
numbers = [1, 2, 3, 4, 5]

# Create a multiprocessing pool with 4 processes
pool = multiprocessing.Pool(4)

# Map the input data to the processing function in parallel
results = pool.map(square, [numbers])

# Print the results
print(results)
