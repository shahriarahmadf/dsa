/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
    let stack = [];

    for (let i=0; i < s.length; i++){
        if (stack.length>0){
            if (stack[stack.length-1] == s[i]){
                stack.pop();
                continue;
            }
        }
        stack.push(s[i]);
    }
    return stack.join('');
};

// Time complexity: O(n)
// Space complexity: O(n)