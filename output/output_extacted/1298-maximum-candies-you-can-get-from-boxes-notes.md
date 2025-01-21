## Maximum Candies You Can Get from Boxes

**Problem Link:** https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description

**Problem Statement:**
- Given a `boxes` list where each element is a list containing two integers, `candies` and `keys`, and a `status` list where each element is a boolean indicating whether the box is open or not.
- The goal is to find the maximum number of candies that can be obtained by opening boxes and using keys to open other boxes.
- The input format is a list of lists `boxes` and a list of booleans `status`.
- The constraints are that `1 <= boxes.length <= 1000`, `boxes[i].length == 2`, `1 <= boxes[i][0] <= 1000`, `0 <= boxes[i][1] <= (1 << 24) - 1`, and `status.length == boxes.length`.
- The expected output is the maximum number of candies that can be obtained.

**Key Requirements and Edge Cases:**
- Handle cases where some boxes are already open and some are not.
- Consider the scenario where a box contains a key that can open another box.
- Identify the condition where a box can be opened using a key from another box.

**Example Test Cases:**
- `boxes = [[1, 1], [2, 2], [3, 3]]`, `status = [true, false, true]`: The maximum number of candies is 6 because we can open the first and third boxes directly and then open the second box using the key from the first box.
- `boxes = [[1, 1], [2, 2], [3, 3]]`, `status = [false, false, false]`: The maximum number of candies is 0 because we cannot open any box without a key.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of opening boxes and using keys to open other boxes.
- We can use a recursive function to explore all possible scenarios and keep track of the maximum number of candies obtained.
- However, this approach is inefficient because it involves a lot of repeated calculations and does not take advantage of the fact that some boxes are already open.

```cpp
int maxCandies(vector<vector<int>>& boxes, vector<bool>& status) {
    int n = boxes.size();
    int maxCandies = 0;
    function<void(int, int)> dfs = [&](int idx, int candies) {
        maxCandies = max(maxCandies, candies);
        for (int i = idx; i < n; i++) {
            if (status[i]) {
                dfs(i + 1, candies + boxes[i][0]);
            }
        }
    };
    dfs(0, 0);
    return maxCandies;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because in the worst case, we need to explore all possible combinations of opening boxes.
> - **Space Complexity:** $O(n)$ because of the recursive function call stack.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of opening boxes, which leads to an exponential time complexity. The space complexity is linear due to the recursive function call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `bitset` to keep track of the keys that have been collected so far.
- We can iterate through the boxes and use the `bitset` to check if we have the key to open a box.
- If we can open a box, we add its candies to the total and update the `bitset` with the new keys.
- We use a `priority_queue` to keep track of the boxes that can be opened next.

```cpp
int maxCandies(vector<vector<int>>& boxes, vector<bool>& status) {
    int n = boxes.size();
    int maxCandies = 0;
    bitset<1001> keys;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < n; i++) {
        if (status[i]) {
            maxCandies += boxes[i][0];
            keys |= (1 << boxes[i][1]);
        }
    }
    for (int i = 0; i < n; i++) {
        if (!status[i] && (keys & (1 << boxes[i][1]))) {
            pq.push(i);
        }
    }
    while (!pq.empty()) {
        int idx = pq.top();
        pq.pop();
        maxCandies += boxes[idx][0];
        keys |= (1 << boxes[idx][1]);
        for (int i = 0; i < n; i++) {
            if (!status[i] && (keys & (1 << boxes[i][1])) && (i != idx)) {
                pq.push(i);
            }
        }
    }
    return maxCandies;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ because we use a `priority_queue` to keep track of the boxes that can be opened next.
> - **Space Complexity:** $O(n)$ because we use a `bitset` to keep track of the keys and a `priority_queue` to keep track of the boxes that can be opened next.
> - **Optimality proof:** This approach is optimal because we use a `bitset` to keep track of the keys and a `priority_queue` to keep track of the boxes that can be opened next, which allows us to explore all possible scenarios efficiently.

---

### Final Notes

**Learning Points:**
- The importance of using a `bitset` to keep track of the keys that have been collected so far.
- The use of a `priority_queue` to keep track of the boxes that can be opened next.
- The need to iterate through the boxes and use the `bitset` to check if we have the key to open a box.

**Mistakes to Avoid:**
- Not using a `bitset` to keep track of the keys, which can lead to inefficient exploration of all possible scenarios.
- Not using a `priority_queue` to keep track of the boxes that can be opened next, which can lead to inefficient exploration of all possible scenarios.
- Not iterating through the boxes and using the `bitset` to check if we have the key to open a box, which can lead to incorrect results.