module.exports = { 
    //param A : array of integers
    //param B : array of integers
    //return an integer
       canCompleteCircuit : function(A, B){
           // A = gas available
           // B = gas required to go to next station
           
           let gas_required = 0;
           let gas_available = 0;
           for (let i = 0; i<A.length; i++){
               gas_available += A[i];
               gas_required += B[i];
           }
           if (gas_required>gas_available){
               return -1;
           }
           
           let gas = 0;
           let station = 0;
           let starting = 0;
           
           while(1){
               gas += A[station]; // take gas from current station
               
               if (B[station] <= gas){
                   // if we have gas to go to next station
                   gas -= B[station];
                   // next station number
                   if (station==A.length-1){
                       // if we are at the last station number
                       station = 0; // go to station 0 (cyclic)                  
                   }else{
                       station++; // go to next station number
                   }
                   // if complete loop has been done
                   if (station == starting){
                       return starting;
                   }
               }else{ // cannot go to the next station
                   // reinitialize from the next station
                   gas = 0;
                   station++;
                   starting = station;
               }            
           }
       }
   };
   