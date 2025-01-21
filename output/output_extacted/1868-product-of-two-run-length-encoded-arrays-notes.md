## Product of Two Run-Length Encoded Arrays

**Problem Link:** https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description

**Problem Statement:**
- Input format: Two run-length encoded arrays `encoded1` and `encoded2`, where each array contains pairs of integers representing the value and frequency of a number in a sequence.
- Constraints: The input arrays are valid run-length encoded arrays.
- Expected output format: A run-length encoded array representing the product of the two input arrays.
- Key requirements and edge cases to consider:
  - Handling arrays of different lengths.
  - Ensuring the output array is correctly formatted as a run-length encoded array.
- Example test cases with explanations:
  - `encoded1 = [[1, 3], [2, 3]]` and `encoded2 = [[6, 3], [2, 3]]`. The expected output should represent the product of the sequences represented by `encoded1` and `encoded2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the product of two run-length encoded arrays, we need to first decode the arrays into their original form, multiply the corresponding elements, and then re-encode the result.
- Step-by-step breakdown of the solution:
  1. Decode both input arrays `encoded1` and `encoded2` into their original sequences.
  2. Multiply the corresponding elements from both sequences.
  3. Re-encode the resulting sequence into a run-length encoded array.

```cpp
vector<vector<int>> productOfEncodedArrays(vector<vector<int>>& encoded1, vector<vector<int>>& encoded2) {
    vector<int> seq1, seq2;
    // Decode encoded1 into seq1
    for (auto& pair : encoded1) {
        int val = pair[0], freq = pair[1];
        for (int i = 0; i < freq; i++) {
            seq1.push_back(val);
        }
    }
    
    // Decode encoded2 into seq2
    for (auto& pair : encoded2) {
        int val = pair[0], freq = pair[1];
        for (int i = 0; i < freq; i++) {
            seq2.push_back(val);
        }
    }
    
    // Calculate the product of seq1 and seq2
    vector<int> product;
    int n = seq1.size(), m = seq2.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            product.push_back(seq1[i] * seq2[j]);
        }
    }
    
    // Re-encode the product into a run-length encoded array
    vector<vector<int>> encodedProduct;
    if (!product.empty()) {
        int currVal = product[0], currCount = 1;
        for (int i = 1; i < product.size(); i++) {
            if (product[i] == currVal) {
                currCount++;
            } else {
                encodedProduct.push_back({currVal, currCount});
                currVal = product[i];
                currCount = 1;
            }
        }
        encodedProduct.push_back({currVal, currCount});
    }
    
    return encodedProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ and $m$ are the lengths of the decoded sequences, and $k$ is the number of distinct elements in the product sequence. The $n \cdot m$ factor comes from generating the product sequence, and the $k$ factor comes from re-encoding the product.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the product sequence.
> - **Why these complexities occur:** The brute force approach involves explicit decoding and re-encoding, leading to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of decoding the arrays into their original sequences, we can directly multiply the corresponding elements from the run-length encoded arrays and then re-encode the result.
- Detailed breakdown of the approach:
  1. Multiply the corresponding elements from `encoded1` and `encoded2`.
  2. Re-encode the resulting sequence into a run-length encoded array.

```cpp
vector<vector<int>> productOfEncodedArrays(vector<vector<int>>& encoded1, vector<vector<int>>& encoded2) {
    vector<vector<int>> encodedProduct;
    for (auto& pair1 : encoded1) {
        for (auto& pair2 : encoded2) {
            int productVal = pair1[0] * pair2[0];
            int productFreq = pair1[1] * pair2[1];
            if (!encodedProduct.empty() && encodedProduct.back()[0] == productVal) {
                encodedProduct.back()[1] += productFreq;
            } else {
                encodedProduct.push_back({productVal, productFreq});
            }
        }
    }
    
    // Re-encode the product into a run-length encoded array
    vector<vector<int>> result;
    if (!encodedProduct.empty()) {
        int currVal = encodedProduct[0][0], currCount = encodedProduct[0][1];
        for (int i = 1; i < encodedProduct.size(); i++) {
            if (encodedProduct[i][0] == currVal) {
                currCount += encodedProduct[i][1];
            } else {
                result.push_back({currVal, currCount});
                currVal = encodedProduct[i][0];
                currCount = encodedProduct[i][1];
            }
        }
        result.push_back({currVal, currCount});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `encoded1` and `encoded2`, respectively.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the product sequence.
> - **Optimality proof:** This approach is optimal because it avoids explicit decoding and re-encoding, reducing the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Run-length encoding and decoding, array multiplication.
- Problem-solving patterns identified: Direct multiplication of encoded arrays.
- Optimization techniques learned: Avoiding explicit decoding and re-encoding.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases, such as empty input arrays.
- Edge cases to watch for: Arrays of different lengths, arrays with duplicate values.
- Performance pitfalls: Using explicit decoding and re-encoding, leading to high time complexity.
- Testing considerations: Test cases with different input sizes, edge cases, and expected outputs.