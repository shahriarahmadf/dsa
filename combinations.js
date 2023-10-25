/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    
    const backtrack = (start,n,k,combination) => {
        if (combination.length == k) {
            result.push([...combination]);
            return;
        }

        for (let i=start; i<=n; i++){
            backtrack(i+1,n,k,combination.concat([i]));
        }
    }

    let result = [];
    backtrack(1,n,k,[]);
    return result;
};