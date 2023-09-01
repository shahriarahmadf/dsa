/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    
    // find the largest binary number digit size
    const largest = Math.max(a.length,b.length);
    // make the smaller digit sized binary to equal sized binary by adding zeros to the left
    if (largest == a.length){
        b = '0'.repeat(largest-b.length) + b;
    }
    else{
        a = '0'.repeat(largest-a.length) + a;
    }

    let ans = '';
    let carry = 0;

    // a loop that runs from the right most index of the binary numbers (both are now same digit sized)
    for (let i=largest-1; i>=0; i--){
        add = parseInt(a[i]) + parseInt(b[i]) + carry;
        carry = 0;

        if (add == 2){
            add = 0;
            carry = 1;
        }
        if(add == 3){
            add = 1;
            carry = 1;
        }
        ans = String(add) + ans;
    }
    if (carry == 1){
        ans = String(carry) + ans;
    }
    return ans;
};