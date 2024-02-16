ex5.md

**QUESTION 1:**

When we try to time a program, some types of issues that may result in an inaccurate measurements would be 
the hardware inconsistencies between different devices, such as CPU speed, and difference in the hardware itself which can affect the measurements accross different devices. Another issue is the inconsistencies in RAM and disk access time, as well as the type of programming language used. 

a. Using the number parameters:
The number parameters approach tries to execute the code 100 times (a large amount of times) and then it returns the total time for all 100 executions. This approach attempts to address the problem by running it many amount of times, in an attempt to reduce the fluctuations and inconsistecies that can happen when trying to time code because it tries to "average out" the time over multiple executions.

b. Using the repeat function:
The repeat function is similar to the number parameters approach by trying to "average out" the time and reduce fluctuations. This repeat function will return a list of 5 different execution times after a piece of code is run 10 times. (Example: repeat 5 times, 10 executions each)

It's appropriate to use the number parameters approach when you want a rough estimate of the pverall performance of the code. It's appropriate to use the repeat function if you want to find out how the performance of the code varies accross multiple tests.

**QUESTION 2:**

a. timeit.timeit(): AVERAGE
Since the .timeit() method returns a single total time for all the executions it's appropriate to only apply the average statistic. Which can be found my dividing the total time by the number of executions.

b. timeit.repeat(): MIN, MAX, AVERAGE
Since the .repeat() method returns a list of multiple execution times, I think it's appropriate to apply all of the aggregate statistics, such as min, max and average. By repeating and recording the execution time multiple times you can identify the fastest, slowest times accross all the tests, as well as calculate the average time.
