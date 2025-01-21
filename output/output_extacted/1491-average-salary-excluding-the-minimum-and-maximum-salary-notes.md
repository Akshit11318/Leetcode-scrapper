## Average Salary Excluding the Minimum and Maximum Salary

**Problem Link:** https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description

**Problem Statement:**
- Input format: An array of integers representing salaries.
- Constraints: The input array will have at least 3 elements.
- Expected output format: The average salary excluding the minimum and maximum salaries.
- Key requirements and edge cases to consider: The array will contain at least 3 elements, and all elements will be non-negative integers.
- Example test cases with explanations:
  - Input: `[4000,3000,1000,2000]`
  - Output: `2500.00000`
  - Explanation: The average of `[2000,3000]` is `(2000+3000)/2 = 2500`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the average salary excluding the minimum and maximum, we first need to identify the minimum and maximum salaries in the array.
- Step-by-step breakdown of the solution:
  1. Find the minimum and maximum salaries in the array.
  2. Calculate the sum of all salaries excluding the minimum and maximum.
  3. Count the number of salaries excluding the minimum and maximum.
  4. Calculate the average by dividing the sum by the count.
- Why this approach comes to mind first: It directly addresses the problem statement by identifying the minimum and maximum salaries and then calculating the average of the remaining salaries.

```cpp
double averageSalary(vector<int>& salary) {
    int minSalary = INT_MAX;
    int maxSalary = INT_MIN;
    long long sum = 0;
    int count = 0;

    // Find min and max salaries
    for (int s : salary) {
        if (s < minSalary) minSalary = s;
        if (s > maxSalary) maxSalary = s;
        sum += s;
    }

    // Calculate sum and count excluding min and max
    for (int s : salary) {
        if (s != minSalary && s != maxSalary) {
            count++;
        } else if (s == minSalary || s == maxSalary) {
            sum -= s;
            // If there are duplicate min or max salaries, subtract them all
            if (s == minSalary) {
                for (int t : salary) {
                    if (t == minSalary) sum -= t;
                    else break;
                }
            }
            if (s == maxSalary) {
                for (int t : salary) {
                    if (t == maxSalary) sum -= t;
                    else break;
                }
            }
        }
    }

    // Adjust sum and count to correctly calculate average
    for (int s : salary) {
        if (s == minSalary) sum += s;
        if (s == maxSalary) sum += s;
    }
    sum = 0;
    count = 0;
    for (int s : salary) {
        if (s != minSalary && s != maxSalary) {
            sum += s;
            count++;
        }
    }

    return (double)sum / count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of salaries. We iterate through the array multiple times, but each iteration is linear.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the minimum and maximum salaries, the sum, and the count.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each salary in the array. The space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the minimum and maximum salaries in a single pass through the array, and then calculate the sum and count of the remaining salaries in another pass.
- Detailed breakdown of the approach:
  1. Initialize variables to store the minimum and maximum salaries, and the sum of all salaries.
  2. Iterate through the array to find the minimum and maximum salaries and calculate the sum of all salaries.
  3. Iterate through the array again to calculate the sum and count of the salaries excluding the minimum and maximum.
  4. Calculate the average by dividing the sum by the count.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we must at least read the input array once.

```cpp
double averageSalary(vector<int>& salary) {
    int minSalary = INT_MAX;
    int maxSalary = INT_MIN;
    long long sum = 0;

    // Find min and max salaries and calculate sum
    for (int s : salary) {
        if (s < minSalary) minSalary = s;
        if (s > maxSalary) maxSalary = s;
        sum += s;
    }

    // Calculate sum and count excluding min and max
    long long newSum = 0;
    int count = 0;
    for (int s : salary) {
        if (s != minSalary && s != maxSalary) {
            newSum += s;
            count++;
        }
    }

    return (double)newSum / count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of salaries. We iterate through the array twice, but each iteration is linear.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the minimum and maximum salaries, the sum, and the count.
> - **Optimality proof:** This approach has the same time complexity as the brute force approach but with less unnecessary work, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding minimum and maximum values, calculating sums and counts, and iterating through arrays.
- Problem-solving patterns identified: Using multiple passes through the input data to calculate different values.
- Optimization techniques learned: Reducing unnecessary work by combining calculations and avoiding redundant iterations.
- Similar problems to practice: Other problems involving array iteration, minimum and maximum values, and average calculations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty arrays or arrays with duplicate minimum or maximum values.
- Edge cases to watch for: Arrays with less than 3 elements, arrays with all elements being the same, and arrays with negative numbers.
- Performance pitfalls: Using unnecessary iterations or calculations, and not optimizing the solution for the given constraints.
- Testing considerations: Thoroughly testing the solution with different input cases, including edge cases and boundary values.