# Assignment No. 14
# Name:vaishnavi Agrahari
# Class:SY-07
# Roll No.:52

# Step 1: Import the logging module
import logging

# Step 2: Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Step 3: Define a function to divide two numbers
def divide_numbers(a, b):
    # Record that the function has started
    logging.info("Division function started")

    # Record input values for debugging
    logging.debug("Values received: a=%s, b=%s", a, b)

    try:
        # Step 4: Perform division
        result = a / b

        # Step 5: Record successful execution
        logging.info("Division successful")

        # Return the calculated result
        return result

    except ZeroDivisionError:
        # Step 6: Record the exception if b is zero
        logging.exception("Cannot divide by zero")

        # Return None to indicate failure
        return None

# Step 7: Record that the program has started
logging.info("Program started")

# Step 8: Call the function with valid input
print("Result:", divide_numbers(10, 2))

# Step 9: Call the function with invalid input
print("Result:", divide_numbers(10, 0))

# Step 10: Record that the program has finished
logging.info("Program finished")

# Step 11: Print a message on the screen
print("Check app.log for execution details.")