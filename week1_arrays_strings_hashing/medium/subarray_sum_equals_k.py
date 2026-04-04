class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        prefix_map = {0:1} # {sum, frequency}

        for num in nums:
            prefix_sum+=num
            #Check if we have seen prefix_sum - k
            if prefix_sum - k in prefix_map:
                count+=prefix_map[prefix_sum-k]
            
            #Store current prefix_sum
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) +1

        return count

  
#HASHMAP CONCEPTS

"""
Alright — let’s strip this down to **first principles** and then connect it to your problem.

---

# 🧠 1. What is a HashMap (super simple)

👉 A HashMap is just a **dictionary (key → value)**

Think:

```text
Name → Phone Number
```

In code:

```python
count = {1: 3, 2: 2}
```

👉 Means:

* number `1` appears 3 times
* number `2` appears 2 times

---

# ⚡ What makes HashMap special?

👉 You can check things **instantly**

```python
if 2 in count:
```

👉 Takes **O(1)** time (very fast)

---

# 🧠 Simple analogy

Think of a locker system:

* You know locker number (key)
* You instantly get what's inside (value)

---

# 🔥 Now connect to YOUR problem

We use hashmap like this:

```python
prefix_map = {0: 1}
```

👉 This means:

> “Sum = 0 has occurred once”

---

# 🧠 What are we storing?

```python
prefix_map[prefix_sum] = frequency
```

👉 We store:

> “How many times have I seen this sum before?”

---

# 📦 Example

```python
nums = [1, -1, 1]
```

We build prefix sums:

```text
1 → 0 → 1
```

Now hashmap becomes:

```text
{
  0: 2,
  1: 2
}
```

---

# 🧠 Why we need this

We use this line:

```python
if prefix_sum - k in prefix_map:
```

👉 Means:

> “Have I seen a previous sum that helps me make k?”

---

# ⚡ Now your main doubt

## ❓ How does this handle NEGATIVE numbers?

---

# 🧠 Key idea (very important)

👉 We are NOT moving window
👉 We are using **math**

---

## Formula:

```text
current_sum - previous_sum = k
```

👉 Rearranged:

```text
previous_sum = current_sum - k
```

---

# 📦 Example with negatives

```python
nums = [1, -1, 1]
k = 1
```

---

## Step-by-step

### Start:

```text
prefix_sum = 0
map = {0:1}
```

---

### Step 1: num = 1

```text
prefix_sum = 1
1 - 1 = 0 → found
```

👉 count = 1

---

### Step 2: num = -1

```text
prefix_sum = 0
0 - 1 = -1 → not found
```

Store:

```text
map = {0:2, 1:1}
```

---

### Step 3: num = 1

```text
prefix_sum = 1
1 - 1 = 0 → found twice!
```

👉 count += 2

---

# 🧠 Why negative doesn’t matter

Because:

👉 We are not comparing values directly
👉 We are comparing **differences between sums**

---

# ⚡ Intuition (this is gold)

Think:

> “If I reached sum = 10 now
> and earlier I saw sum = 7
> then everything in between = 3”

---

# 🎯 One-line understanding

👉

```text
HashMap stores past sums so we can quickly check if a valid subarray exists
```

---

# 🔚 Final takeaway

* HashMap = fast memory (store & lookup)
* We store prefix sums
* We check `(prefix_sum - k)`
* Works even with negatives because it's math-based, not direction-based

---

If you want next:
👉 I can give you a **2-minute mental template** to solve any hashmap problem instantly (very useful for interviews)

"""


