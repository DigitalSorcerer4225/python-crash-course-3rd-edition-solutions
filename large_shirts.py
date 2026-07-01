# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large  by default with a message that reads I love Python. Make a large shirt and a  medium shirt with the default message, and a shirt of any size with a different  message. 

def make_shirt(message, size="Large"):
    print("Making your t-shirt...")
    print(f"Selecting Size: {size.title()}...done")
    print(f"Adding Message: {message}...done")
    print(f"Here is the shirt you've requested.")

make_shirt("I love Python!")
make_shirt('I love Python!', 'medium')
make_shirt(':)', 'small')