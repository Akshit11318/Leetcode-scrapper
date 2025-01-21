## Describe the Painting
**Problem Link:** https://leetcode.com/problems/describe-the-painting/description

**Problem Statement:**
- Input format and constraints: The input is an array of `split` pairs, where each pair contains two integers representing the start and end of a split. The array can have any number of splits.
- Expected output format: The function should return a vector of vectors, where each inner vector contains the start and end of a segment in the painting, along with the color of the segment.
- Key requirements and edge cases to consider: 
    - Segments can overlap, and the function should handle this by combining overlapping segments of the same color.
    - If two segments overlap but have different colors, the function should split them into separate segments.
- Example test cases with explanations:
    - Example 1: `split = [[1,3],[2,4],[3,6],[4,5]]`, `colors = ["a","b","c","d"]`. The output should be `[[1,3,"a"],[3,4,"b"],[4,5,"c"],[5,6,"d"]]`.
    - Example 2: `split = [[1,4],[1,5]]`, `colors = ["a","b"]`. The output should be `[[1,4,"a"],[4,5,"b"]]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each segment in the `split` array and checking for overlaps with previous segments.
- Step-by-step breakdown of the solution: 
    1. Sort the segments by their start value.
    2. Iterate over each segment and check for overlaps with previous segments.
    3. If an overlap is found, merge the segments if they have the same color, or split them if they have different colors.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient for large inputs due to its $O(n^2)$ time complexity.

```cpp
vector<vector<int>> describePainting(vector<vector<int>>& split, vector<string>& colors) {
    vector<vector<int>> segments;
    for (int i = 0; i < split.size(); i++) {
        vector<vector<int>> newSegments;
        for (auto segment : segments) {
            if (segment[1] < split[i][0]) {
                newSegments.push_back(segment);
            } else if (split[i][1] < segment[0]) {
                newSegments.push_back(segment);
            } else if (segment[2] == colors[i]) {
                newSegments.push_back({min(segment[0], split[i][0]), max(segment[1], split[i][1]), colors[i]});
            } else {
                newSegments.push_back({min(segment[0], split[i][0]), segment[0], segment[2]});
                newSegments.push_back({segment[0], max(segment[1], split[i][1]), colors[i]});
                newSegments.push_back({max(segment[1], split[i][1]), max(segment[1], split[i][1]), segment[2]});
            }
        }
        if (segments.empty()) {
            newSegments.push_back({split[i][0], split[i][1], colors[i]});
        }
        segments = newSegments;
    }
    return segments;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of segments. This is because in the worst case, we are iterating over all segments for each segment.
> - **Space Complexity:** $O(n)$, where $n$ is the number of segments. This is because we are storing all segments in the `segments` vector.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are using a nested loop to iterate over all segments. The space complexity is $O(n)$ because we are storing all segments in the `segments` vector.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sweep line algorithm to solve this problem efficiently. The idea is to sort all events (start and end of segments) and process them in order.
- Detailed breakdown of the approach: 
    1. Create a vector of events, where each event is a pair containing the position and a boolean indicating whether it's a start or end event.
    2. Sort the events by position.
    3. Iterate over the events and maintain a set of active segments.
    4. When a start event is encountered, add the corresponding segment to the set of active segments.
    5. When an end event is encountered, remove the corresponding segment from the set of active segments.
    6. If the set of active segments changes, add a new segment to the result vector.
- Proof of optimality: This approach is optimal because it only requires a single pass over the events, resulting in a time complexity of $O(n \log n)$.

```cpp
vector<vector<int>> describePainting(vector<vector<int>>& split, vector<string>& colors) {
    vector<vector<int>> events;
    for (int i = 0; i < split.size(); i++) {
        events.push_back({split[i][0], 1, i});
        events.push_back({split[i][1], -1, i});
    }
    sort(events.begin(), events.end());
    set<pair<string, int>> activeSegments;
    vector<vector<int>> result;
    int start = -1;
    for (auto event : events) {
        if (event[1] == 1) {
            activeSegments.insert({colors[event[2]], event[2]});
        } else {
            activeSegments.erase({colors[event[2]], event[2]});
        }
        if (start == -1) {
            start = event[0];
        }
        if (activeSegments.size() == 1) {
            if (result.empty() || result.back()[2] != (*activeSegments.begin()).first) {
                if (result.size() > 0 && result.back()[1] == start) {
                    result.back()[1] = event[0];
                } else {
                    result.push_back({start, event[0], (*activeSegments.begin()).first});
                }
            }
        } else if (activeSegments.size() == 0) {
            if (result.size() > 0 && result.back()[1] == event[0]) {
                result.back()[1] = event[0];
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of segments. This is because we are sorting the events.
> - **Space Complexity:** $O(n)$, where $n$ is the number of segments. This is because we are storing all events and active segments.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the events, resulting in a time complexity of $O(n \log n)$. The space complexity is also optimal because we are only storing the necessary information.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sweep line algorithm, event handling.
- Problem-solving patterns identified: Handling overlapping segments, maintaining active segments.
- Optimization techniques learned: Reducing time complexity by using a sweep line algorithm.
- Similar problems to practice: Other problems involving sweep line algorithms, such as finding the maximum number of overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not maintaining active segments correctly.
- Edge cases to watch for: Overlapping segments, segments with the same color.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing with different inputs, including edge cases and large inputs.