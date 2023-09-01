/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // converting all to lower case
    s = s.toLowerCase();

    // new string where only letters and number digits will be included 
    let s_new = '';

    // loop through the original string to get s_new 
    for (let i=0; i< s.length; i++){
        if ( (s[i] >= 'a' && s[i]<='z') || (s[i]>='0' && s[i]<='9') ){
            s_new = s_new + s[i];
        }
    }

    // compare first with last, then second with second last, ... until middle element
    for (let i=0; i <= Math.floor(s_new.length/2); i++){
        if (s_new[i] != s_new[(s_new.length)-1-i]){
            return false
        }
    }
    return true
};