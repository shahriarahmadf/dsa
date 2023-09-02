/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let req_ending_brackets = [];

    const bracket_mapping = {
        '(':')',
        '{':'}',
        '[':']'
    };
    for (const x of s){
        if (bracket_mapping.hasOwnProperty(x)){
            req_ending_brackets.push(bracket_mapping[x]);
        }
        else if(Object.values(bracket_mapping).includes(x)){
            if (req_ending_brackets.length == 0){
                return false;
            }
            else if(req_ending_brackets[req_ending_brackets.length-1] == x){
                req_ending_brackets.pop();
            }
            else{
                return false;
            }
        }
    }
    if (req_ending_brackets.length == 0){
        return true;
    }
    else{
        return false;
    }
};

// Time complexity: O(n)
// Space complexity: O(n)