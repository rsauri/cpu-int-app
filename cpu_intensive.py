# cpu_intensive.py

def calculate_pi(num_terms):
    pi = 0
    for k in range(num_terms):
        pi += ((-1) ** k) / (2 * k + 1)
    return 4 * pi

if __name__ == "__main__":
    num_terms = 10000000  # Increase this number for more CPU-intensive task
    result = calculate_pi(num_terms)
    print(f"Approximation of pi with {num_terms} terms: {result}")

