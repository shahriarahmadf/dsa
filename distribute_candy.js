module.exports = { 
    //param A : array of integers
    //return an integer
       candy : function(A){
           let candy = [];
   
           for (let i=0;i<A.length;i++){
               candy.push(1);
           }
           for (let i=1; i<=A.length;i++){
               if(A[i]>A[i-1]){
                   candy[i] = candy[i-1] + 1;
               }
           }
           for (let i=A.length-2;i>=0;i--){
               if(A[i]>A[i+1]){
                   candy[i] = Math.max(candy[i],candy[i+1]+1);
               }
           }
   
           let total_candies = 0;
           for (let i=0;i<candy.length;i++){
               total_candies += candy[i];
           }
           return total_candies;
       }
   };
   