## Encode and Decode TinyURL
**Problem Link:** https://leetcode.com/problems/encode-and-decode-tinyurl/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a `TinyURL` system that can encode and decode URLs. The input for encoding is a long URL, and the output should be a unique short URL. The input for decoding is a short URL, and the output should be the original long URL.
- Expected output format: For encoding, the output should be a string representing the short URL. For decoding, the output should be a string representing the original long URL.
- Key requirements and edge cases to consider: The system should handle a large number of URLs, ensure uniqueness of short URLs, and be efficient in terms of time and space complexity.
- Example test cases with explanations: 
    - Encoding "https://leetcode.com/problems/design-tinyurl" should return a unique short URL like "http://tinyurl.com/4e9iAk".
    - Decoding "http://tinyurl.com/4e9iAk" should return "https://leetcode.com/problems/design-tinyurl".

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One might start by thinking of storing all the long URLs in a database and assigning a unique identifier to each one. However, this approach doesn't directly provide a short URL.
- Step-by-step breakdown of the solution:
    1. Store all long URLs in a database or a map.
    2. Assign a unique identifier to each long URL.
    3. For encoding, generate a random short URL and store it in the database with its corresponding long URL.
    4. For decoding, look up the short URL in the database and return the corresponding long URL.
- Why this approach comes to mind first: It's a straightforward way to ensure uniqueness and handle encoding and decoding.

```cpp
class TinyURL {
private:
    unordered_map<string, string> longToShort;
    unordered_map<string, string> shortToLong;
    string base = "http://tinyurl.com/";
    int counter = 0;

public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        if (longToShort.find(longUrl) != longToShort.end()) {
            return longToShort[longUrl];
        }
        string shortUrl = base + to_string(counter);
        longToShort[longUrl] = shortUrl;
        shortToLong[shortUrl] = longUrl;
        counter++;
        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        if (shortToLong.find(shortUrl) != shortToLong.end()) {
            return shortToLong[shortUrl];
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for both encoding and decoding, assuming the hash operations are constant time.
> - **Space Complexity:** $O(N)$, where $N$ is the number of URLs, because we're storing all URLs in memory.
> - **Why these complexities occur:** The time complexity is constant because we're using hash tables for lookups. The space complexity is linear because we're storing all URLs.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight here is to use a hash function to map long URLs to short URLs directly, without needing a counter or a database. This approach can utilize a base62 encoding scheme to generate short URLs that are more compact and URL-friendly.
- Detailed breakdown of the approach:
    1. Design a base62 encoding function to convert integers to short URLs.
    2. Use a hash function to map long URLs to integers.
    3. For encoding, use the hash function to get an integer, then convert it to a base62 short URL.
    4. For decoding, store the mapping of short URLs to long URLs in a hash table.
- Proof of optimality: This approach is optimal because it minimizes the length of the short URL while ensuring uniqueness and efficient lookup.
- Why further optimization is impossible: Given the constraints of the problem, any further optimization would likely compromise on either uniqueness, efficiency, or the length of the short URL.

```cpp
class TinyURL {
private:
    unordered_map<string, string> urlMap;
    string base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int counter = 0;

public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        if (urlMap.find(longUrl) != urlMap.end()) {
            return urlMap[longUrl];
        }
        string shortUrl = "http://tinyurl.com/" + toBase62(counter);
        urlMap[longUrl] = shortUrl;
        urlMap[shortUrl] = longUrl;
        counter++;
        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        if (urlMap.find(shortUrl) != urlMap.end()) {
            return urlMap[shortUrl];
        }
        return "";
    }

    string toBase62(int num) {
        string res;
        while (num > 0) {
            res = base62[num % 62] + res;
            num /= 62;
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for both encoding and decoding, assuming the hash operations and base62 conversion are constant time.
> - **Space Complexity:** $O(N)$, where $N$ is the number of URLs, because we're storing all URLs in memory.
> - **Optimality proof:** The time complexity is constant because we're using hash tables for lookups and a base62 encoding scheme that's efficient. The space complexity is linear because we're storing all URLs.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Hash tables, base62 encoding.
- Problem-solving patterns identified: Using hash functions for efficient lookups, designing compact encoding schemes.
- Optimization techniques learned: Minimizing the length of the short URL while ensuring uniqueness and efficiency.
- Similar problems to practice: URL shortening services, compact encoding schemes.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., empty URLs), not ensuring uniqueness of short URLs.
- Edge cases to watch for: Empty URLs, very long URLs, URLs that are already shortened.
- Performance pitfalls: Using inefficient data structures or encoding schemes.
- Testing considerations: Test with a variety of URLs, including edge cases, to ensure correctness and efficiency.