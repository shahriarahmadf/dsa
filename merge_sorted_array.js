function merger(nums1, nums2, m, n) {
    let i = m-1;
    let j = n-1;
    let k = m+n-1;

    while ( (i>=0) && (j>=0) ){
        if (nums1[i] >= nums2[j]){
            nums1[k] = nums1[i];
            i--;
        }
        else{
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }

    // in case nums2 still has some elements left to be looped through
    // we dont have to consider for nums1 because 
    // we are replacing in place of nums1 elements anyway
    while (j>=0){
        nums1[k] = nums2[j];
        j--;
        k--;
    }
}

// Time complexity: O(m+n)
// Space complexity: O(1)