module.exports = { 
  //param A : array of array of integers
  //return an integer
   solve : function(A){
         let meetings = [];
         
         A.map( x => {
             meetings.push( [x[0],1] ); // start time encoded with 1
             meetings.push( [x[1],0] ); // end time encoded with 0
         })
         meetings.sort((a,b) => a[0] - b[0]);        
         let room = 0;
         let max_room = 0;
         meetings.map(x => {
             if (x[1] == 1){
                 room += 1;
             }
             else {
                 room -= 1;
             }
             max_room = Math.max(room,max_room);
         })
         return max_room;
   }
 };
 