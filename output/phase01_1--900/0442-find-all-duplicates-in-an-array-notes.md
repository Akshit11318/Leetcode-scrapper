## Find All Duplicates in an Array
**Problem Link:** https://leetcode.com/problems/find-all-duplicates-in-an-array/description

**Problem Statement:**
- Given an array of integers `nums` containing `n` integers where each integer is in the range `[1, n]` and may appear only once or twice, return all the duplicates in the array.
- Input format: An array of integers
- Constraints: `1 <= n <= 10^4`, `1 <= nums[i] <= n`
- Expected output format: A vector of integers representing the duplicates found in the array
- Key requirements: Identify all numbers that appear more than once in the array
- Edge cases: Empty array, array with all unique elements, array with all duplicate elements
- Example test cases:
  - Input: `[4,3,2,7,8,2,3,1]`, Output: `[2,3]`
  - Input: `[1,1,2]`, Output: `[1]`
  - Input: `[1]`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the array and checking for each element if it has been encountered before. This can be achieved using an additional data structure to keep track of encountered elements.
- Step-by-step breakdown:
  1. Initialize an empty vector `duplicates` to store the duplicate elements.
  2. Create a set `encountered` to keep track of elements we have seen so far.
  3. Iterate through the array `nums`. For each element:
    - Check if the element is already in the `encountered` set.
    - If it is, add the element to the `duplicates` vector (if it's not already there) since it's a duplicate.
    - If not, add the element to the `encountered` set.
  4. Return the `duplicates` vector.

```cpp
vector<int> findDuplicates(vector<int>& nums) {
    vector<int> duplicates;
    set<int> encountered;
    
    for (int num : nums) {
        if (encountered.find(num) != encountered.end()) {
            if (find(duplicates.begin(), duplicates.end(), num) == duplicates.end()) {
                duplicates.push_back(num);
            }
        } else {
            encountered.insert(num);
        }
    }
    
    return duplicates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the iteration through the array, where $n$ is the number of elements in the array, and $O(1)$ for the set operations (insertion and search), making the overall time complexity $O(n)$. However, the `find` operation in the vector `duplicates` takes $O(m)$ where $m$ is the number of duplicates found so far, leading to an overall complexity of $O(n + m^2)$ in the worst case.
> - **Space Complexity:** $O(n)$ for storing the `encountered` set and the `duplicates` vector.
> - **Why these complexities occur:** The iteration through the array and the set operations are linear, but the search within the `duplicates` vector can lead to a quadratic term in the worst case.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can utilize the fact that the numbers in the array are in the range `[1, n]`, where `n` is the number of elements in the array. We can treat the array itself as a hash table where the index represents the number minus one. By iterating through the array and marking the corresponding index for each number, we can identify duplicates based on the marking.
- Detailed breakdown:
  1. Initialize an empty vector `duplicates` to store the duplicate elements.
  2. Iterate through the array `nums`. For each element `num`:
    - Calculate the index `idx = abs(num) - 1`.
    - If the value at `nums[idx]` is negative, it means we've seen `abs(num)` before, so add `abs(num)` to the `duplicates` vector.
    - Otherwise, mark `nums[idx]` as negative.
  3. Return the `duplicates` vector.

```cpp
vector<int> findDuplicates(vector<int>& nums) {
    vector<int> duplicates;
    
    for (int num : nums) {
        int idx = abs(num) - 1;
        if (nums[idx] < 0) {
            if (find(duplicates.begin(), duplicates.end(), abs(num)) == duplicates.end()) {
                duplicates.push_back(abs(num));
            }
        } else {
            nums[idx] *= -1;
        }
    }
    
    return duplicates;
}
```

However, we can simplify the code and improve it by directly using the array without an additional `find` operation:

```cpp
vector<int> findDuplicates(vector<int>& nums) {
    vector<int> duplicates;
    
    for (int i = 0; i < nums.size(); i++) {
        int idx = abs(nums[i]) - 1;
        if (nums[idx] < 0) {
            duplicates.push_back(abs(nums[i]));
        } else {
            nums[idx] *= -1;
        }
    }
    
    return duplicates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we perform a constant amount of work for each element.
> - **Space Complexity:** $O(1)$ excluding the space needed for the output, because we only use a constant amount of space to store the `duplicates` vector, and we modify the input array in-place.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the array, using the array itself as extra space for marking visited indices, thus minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Utilizing the constraints of the problem (e.g., the range of numbers) to optimize the solution.
- Modifying the input array in-place to reduce space complexity.
- Avoiding unnecessary data structures and operations.

**Mistakes to Avoid:**
- Not considering the constraints of the problem, leading to inefficient solutions.
- Not optimizing the solution for the specific characteristics of the input data.
- Failing to consider the trade-offs between time and space complexity.