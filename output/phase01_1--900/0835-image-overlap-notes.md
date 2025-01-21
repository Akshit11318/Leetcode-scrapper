## Image Overlap
**Problem Link:** https://leetcode.com/problems/image-overlap/description

**Problem Statement:**
- Input format: Two binary images, each represented as a 2D array (`img1` and `img2`).
- Constraints: The images are binary (0s and 1s), and their dimensions are within the range of 1 to 31.
- Expected output format: The largest possible overlap between `img1` and `img2`.
- Key requirements and edge cases to consider: The overlap can be achieved by shifting `img1` in any of the eight directions (up, down, left, right, and four diagonals) relative to `img2`. The goal is to maximize the overlap, which is the sum of the number of positions at which the corresponding pixels of `img1` and `img2` are both 1 after shifting.
- Example test cases with explanations:
  - When `img1 = [[1,1,0],[0,1,0],[0,1,0]]` and `img2 = [[0,0,0],[0,1,1],[0,0,1]]`, the maximum overlap is 3, achieved by shifting `img1` one position to the right and one position down relative to `img2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum overlap, we can try all possible shifts of `img1` relative to `img2` and calculate the overlap for each shift.
- Step-by-step breakdown of the solution:
  1. Define all possible shifts (up, down, left, right, and four diagonals).
  2. For each possible shift, apply the shift to `img1`.
  3. Calculate the overlap between the shifted `img1` and `img2` by summing the positions where both images have a pixel value of 1.
  4. Keep track of the maximum overlap found among all shifts.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered.

```cpp
int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
    int n = img1.size();
    int maxOverlap = 0;
    
    // Define all possible shifts
    for (int dx = -n + 1; dx < n; dx++) {
        for (int dy = -n + 1; dy < n; dy++) {
            int overlap = 0;
            // Calculate overlap for current shift
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i + dx >= 0 && i + dx < n && j + dy >= 0 && j + dy < n) {
                        overlap += img1[i][j] & img2[i + dx][j + dy];
                    }
                }
            }
            // Update max overlap
            maxOverlap = max(maxOverlap, overlap);
        }
    }
    
    return maxOverlap;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the images. This is because for each possible shift ($O(n^2)$), we are iterating over the entire image ($O(n^2)$) to calculate the overlap.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach checks every possible shift, leading to a high time complexity. However, it only uses a constant amount of space to store the maximum overlap, resulting in a low space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of shifting the images and calculating overlaps, we can count the number of times each pair of pixels (one from `img1` and one from `img2`) appears at the same relative position. This can be achieved by considering the vector difference between pixel positions in `img1` and `img2`.
- Detailed breakdown of the approach:
  1. Iterate over all pixels in both images.
  2. For each pair of pixels that are both 1, calculate the vector difference in their positions.
  3. Use a hashmap to count the occurrences of each vector difference.
  4. The maximum count in the hashmap represents the maximum overlap.
- Proof of optimality: This approach ensures that we consider all possible overlaps without explicitly shifting the images, reducing the time complexity significantly.

```cpp
int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
    int n = img1.size();
    unordered_map<string, int> count;
    int maxOverlap = 0;
    
    // Count occurrences of each vector difference
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (img1[i][j] == 1) {
                for (int x = 0; x < n; x++) {
                    for (int y = 0; y < n; y++) {
                        if (img2[x][y] == 1) {
                            string key = to_string(x - i) + "," + to_string(y - j);
                            count[key]++;
                            maxOverlap = max(maxOverlap, count[key]);
                        }
                    }
                }
            }
        }
    }
    
    return maxOverlap;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, because in the worst case, every pixel in `img1` is 1, and for each of these, we iterate over all pixels in `img2`.
> - **Space Complexity:** $O(n^2)$, as in the worst case, we might store every possible vector difference in the hashmap.
> - **Optimality proof:** While the time complexity remains $O(n^4)$ due to the nested loops over both images, this approach is more efficient in practice because it avoids the overhead of explicit shifts and uses a hashmap for efficient counting. However, it's worth noting that the problem's nature inherently leads to a high time complexity due to the need to consider all pairs of pixels.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Brute force approach, hashmap usage for counting occurrences, and the concept of vector differences for relative positioning.
- Problem-solving patterns identified: The importance of considering all possible scenarios (in this case, all shifts or all pairs of pixels), and optimizing the approach by using more efficient data structures and algorithms.
- Optimization techniques learned: Avoiding explicit shifts by using vector differences and employing hashmaps for efficient counting.
- Similar problems to practice: Other problems involving image processing, pattern recognition, or relative positioning, such as template matching or feature detection.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing when calculating shifts or vector differences, and not handling edge cases properly (e.g., when a shift would move a pixel out of the image bounds).
- Edge cases to watch for: Images with all zeros, images with all ones, and images with specific patterns that could lead to incorrect overlap calculations if not handled carefully.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexities.
- Testing considerations: Thoroughly testing the implementation with various input images, including edge cases, to ensure correctness and efficiency.