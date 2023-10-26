module.exports = { 
    //param A : string
    //return a array of strings
       letterCombinations : function(A){
           const backtrack = (buttons,A,currentLetters) => {
               if (A.length == 0){
                   result.push(currentLetters.join(''));
                   return;
               }
               
               let newCurrentLetters = [];
               
               for (let x of currentLetters){
                   for (let y of buttons[A[0]]){
                       newCurrentLetters.push(x+y);
                   }
               }
               currentLetters = newCurrentLetters;
               
               for (let currentLetter of currentLetters){
                   backtrack(buttons,A.slice(1),[currentLetter]);
               }
               
           }
           
           let result = [];
           
           const buttons = {
               '0': ['0'],
               '1': ['1'],
               '2': ['a','b','c'],
               '3': ['d','e','f'],
               '4': ['g','h','i'],
               '5': ['j','k','l'],
               '6': ['m','n','o'],
               '7': ['p','q','r','s'],
               '8': ['t','u','v'],
               '9': ['w','x','y','z']
           };
           
           backtrack(buttons,A,['']);
           
           return result;       
       }
   };
   