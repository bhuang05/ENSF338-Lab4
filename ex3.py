import sys

"""
1.The strategy for growing arrays when full is discussed in lines 60-69 of the code. After looking at the following lines, the growth factor seems to be 1.125 or 9/8.

2. unfinished questions + code.






"""

# ChatGPT used to do #2.
def main():
    list = []
    previous_size = sys.getsizeof(list)

    # Loop from 0 to 63
    for i in range(64):
        # Append a new integer to the list
        list.append(i)
        # Check the current size of the list
        current_size = sys.getsizeof(list)
        # If the size has changed, print a message
        if current_size != previous_size:
            print(f"Size changed at element {i}: from {previous_size} to {current_size} bytes")
            previous_size = current_size

if __name__ == "__main__":
    main()