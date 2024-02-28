import sys
import timeit

"""
1.The strategy for growing arrays when full is discussed in lines 60-69 of the code. The strategy involves over-allocating memory to the array beyond the current size in case more elements need to be added. This is shown in line 70:     

new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;

After looking at the following lines, the growth factor seems to be 1.125 or 9/8.

5. Looking at the output of the graph, the bars for the histogram mostly seem to overlap. This indicates that there is little to no difference between growing the array from size S-1 to S and S to S + 1. Because of the over-allocation strategy, it avoids resizing everytime a new element is added, and this applies for both cases. 
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
    
    '''
    The code below is for questions #3 and #4.
    '''
    S = 63

    # Measure the time it takes to grow the array from size S to S+1
    time_to_grow_s_to_s_plus_1 = timeit.repeat(lambda: [0] * S + [0], number=1, repeat=1000)

    # Measure the time it takes to grow the array from size S-1 to S
    time_to_grow_s_minus_1_to_s = timeit.repeat(lambda: [0] * (S - 1) + [0], number=1, repeat=1000)

    # Plotting the distribution of both measurements
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))

    plt.hist(time_to_grow_s_to_s_plus_1, bins=30, alpha=0.5, label='Time to grow from S to S+1')
    plt.hist(time_to_grow_s_minus_1_to_s, bins=30, alpha=0.5, label='Time to grow from S-1 to S')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    plt.title('Distribution of Time Measurements for List Growth')
    plt.show()
            

if __name__ == "__main__":
    main()