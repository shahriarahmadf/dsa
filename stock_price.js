
const stockPrice = prices => {
    let profit = 0;
    let current_profit = 0;
    let end = -1;
    let start = prices[0];

    for (let i=1; i<prices.length; i++){
        if (prices[i] < start){
            start = prices[i];
        }
        else{
            current_profit = prices[i] - start;
            if (current_profit>profit){
                profit =  current_profit;
                end = i;
            }
        }
    }
    return (end+1)
}
console.log(stockPrice([7,1,5,3,6,4]));
console.log(stockPrice([7,6,4,3,1]));

// time complexity: O(n)
// space complexity: O(n)
