/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let total = -1e5;
    let total_max = -1e5;

    for (let i=0; i<nums.length; i++){
        if ( nums[i] > (total+nums[i]) ){
            total = nums[i]
        }
        else{
            total += nums[i];
        }
        if (total > total_max){
            total_max = total;
        }
    }    
    return total_max;
};