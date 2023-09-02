const multiplication_without_star = (a,b,multiplicator) => {
    if (multiplicator == undefined){
        // swap a and b, when function runs for first time, for optimization
        a = a + b;
        b = a - b;
        a = a - b;
        //
        multiplicator = a;
    }
    
    // base case
    if (b == 1){
        return a;
    }
    else{
        a += multiplicator;
        return multiplication_without_star(a,b-1,multiplicator);
    }
}

console.log(multiplication_without_star(6,2));

// Time complexity: O(n)
// Space complexity: O(n)