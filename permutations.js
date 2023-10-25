/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    
    const backtrack = (nums,currentPerm) => {
        if (nums.length == 0){
            result.push([...currentPerm]);
            return;
        }
        for (let x=0; x<nums.length; x++){
            const remaining = nums.slice(0,x).concat(nums.slice(x+1));
            backtrack(remaining, currentPerm.concat([nums[x]]));
        }
    }
    
    let result = [];
    backtrack(nums,[]);
    return result;
};