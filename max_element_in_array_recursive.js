const findMax_recursion = array => {

    // base case
    if (array.length == 1){
        return array[0];
    }
    // recursive case
    if ( array[array.length-1] > array[array.length-2] ){
        array[array.length-2] = array[array.length-1];
    }
    array.pop();
    return findMax_recursion(array);
}

console.log(findMax_recursion([3,10,-3,12,5,12,-61,2313,2]));