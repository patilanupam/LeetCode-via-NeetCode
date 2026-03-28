def merge(nums1, m, nums2, n):
    i = m - 1  # last valid element in nums1
    j = n - 1  # last element in nums2
    k = m + n - 1  # last position in nums1 (including empty space)

    # thinking:
    # fill from the back so we don't overwrite useful data in nums1

    while i >= 0 and j >= 0:
        # place the larger element at the end
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    # if nums2 still has elements, copy them
    # (no need to copy nums1 leftovers — they’re already in place)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Time Complexity: O(m + n) - we go through both arrays once
# Space Complexity: O(1) - we merge in place without extra space