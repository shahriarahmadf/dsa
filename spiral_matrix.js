/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {

    let count = matrix.length * matrix[0].length;

    let top = 0;
    let bottom = matrix.length-1;
    let left = 0;
    let right = matrix[0].length-1;

    let output = [];

    while(count>0){

        // left to right = col increase, row same
        for (let i = left; i<=right ; i++){
            output.push(matrix[top][i]);
            count -= 1;
        }
        top += 1;

        if (count == 0){
            break;
        }

        // top to bottom = row increase, col same
        for (let i = top; i<=bottom ; i++){
            output.push(matrix[i][right]);
            count -= 1;
        }
        right -= 1;

        if (count == 0){
            break;
        }

        // right to left = col decrease, row same
        for (let i = right; i>=left ; i--){
            output.push(matrix[bottom][i]);
            count -= 1;
        }
        bottom -= 1;

        if (count == 0){
            break;
        }

        // bottom to top = row decrease, col same
        for (let i = bottom; i>=top ; i--){
            output.push(matrix[i][left]);
            count -= 1;
        }
        left += 1;

        if (count == 0){
            break;
        }
    }
    return output;

};