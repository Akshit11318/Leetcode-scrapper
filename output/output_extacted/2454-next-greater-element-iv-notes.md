## Next Greater Element IV
**Problem Link:** https://leetcode.com/problems/next-greater-element-iv/description

**Problem Statement:**
- Given two arrays `nums1` and `nums2`, find all the next greater elements of `nums1` in `nums2`. 
- The next greater element of a number `x` in `nums1` is the first greater number to its right in `nums2`. If it does not exist, return `-1` for this number.
- Input arrays are non-empty and contain only integers.
- Expected output format is an array of integers where each integer is the next greater element of the corresponding element in `nums1`.

**Example Test Cases:**
- `nums1 = [4,1,2]`, `nums2 = [1,3,4,2]`, output: `[-1,3,-1]`
- `nums1 = [2,4]`, `nums2 = [1,2,3,4]`, output: `[2,3]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each element in `nums1` and finding its next greater element in `nums2`.
- For each element in `nums1`, we iterate over `nums2` from left to right to find the first element greater than the current element from `nums1`.
- This approach is straightforward but inefficient due to the nested loop structure.

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    vector<int> result;
    for (int num : nums1) {
        bool found = false;
        for (int i = 0; i < nums2.size(); i++) {
            if (nums2[i] == num) {
                for (int j = i + 1; j < nums2.size(); j++) {
                    if (nums2[j] > num) {
                        result.push_back(nums2[j]);
                        found = true;
                        break;
                    }
                }
                break;
            }
        }
        if (!found) {
            result.push_back(-1);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the size of `nums1` and $m$ is the size of `nums2`, due to the nested loop structure.
> - **Space Complexity:** $O(n)$, where $n$ is the size of `nums1`, for storing the result.
> - **Why these complexities occur:** The brute force approach involves iterating over each element in `nums1` and then over `nums2` to find the next greater element, resulting in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a stack to store the indices of the elements in `nums2` that we have not yet found a greater element for.
- We iterate over `nums2`, and for each element, we pop all the elements from the stack that are smaller than the current element and update our result array with the current element as the next greater element.
- We then push the current index onto the stack.
- After iterating over `nums2`, we iterate over `nums1` and find the next greater element for each element in `nums1` by checking if it exists in our result array.

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> st;
    for (int num : nums2) {
        while (!st.empty() && st.top() < num) {
            map[st.top()] = num;
            st.pop();
        }
        st.push(num);
    }
    vector<int> result;
    for (int num : nums1) {
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } else {
            result.push_back(-1);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums1` and $m$ is the size of `nums2`, due to the single pass over `nums1` and `nums2`.
> - **Space Complexity:** $O(n + m)$, for storing the stack and the result array.
> - **Optimality proof:** This approach is optimal because we only make a single pass over `nums1` and `nums2`, resulting in the best possible time complexity.

---

### Final Notes

**Learning Points:**
- Using a stack to keep track of elements that we have not yet found a greater element for.
- Utilizing an unordered map to store the next greater element for each element in `nums2`.
- Optimizing the solution by reducing the number of iterations over the input arrays.

**Mistakes to Avoid:**
- Not considering the use of a stack to improve the efficiency of the solution.
- Not utilizing an unordered map to store the next greater element for each element in `nums2`.
- Not optimizing the solution by reducing the number of iterations over the input arrays.