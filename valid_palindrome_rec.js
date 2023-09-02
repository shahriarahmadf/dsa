function validPalindrome (text) {

    // base case
    if (text.length <= 1){
        return true;
    }

    // recursive case
    if (text[0] == text[text.length-1]) {
        return validPalindrome(text.slice(1,text.length-1));
    }
    else{
        return false;
    }
}
console.log(validPalindrome('madam'));