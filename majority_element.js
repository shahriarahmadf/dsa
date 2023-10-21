module.exports = { 
    //param A : array of integers
    //return an integer
       majorityElement : function(A){
       A.sort();
       const size = Math.floor(A.length / 2);
       let count = 0;
       let current = null;
   
       for (let i = 0; i < A.length; i++) {
           if (current == A[i]) {
               count++;
           } else {
               current = A[i];
               count = 1;
           }
           if (count > size) {
               return Number(current);
           }
       }
   }}