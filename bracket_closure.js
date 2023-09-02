const bracket_closure = s => {
    let req_ending_brackets = [];
    let pointer = 0;

    for (const x of s){
        if (x == '('){
            req_ending_brackets.push(')');
        }
        else if (x == '{'){
            req_ending_brackets.push('}');
        }
        else if (x == '['){
            req_ending_brackets.push(']');
        }
        else if (x == ')' || x == '}' || x == ']'){
            if (req_ending_brackets[pointer] == x){
                req_ending_brackets[pointer] = 0;
                pointer += 1
            }
            else{
                break;
            }
        }
    }
    if (pointer == req_ending_brackets.length){
        return true;
    }
    else{
        return false;
    }
}
// test cases
console.log(bracket_closure('()')); //true
console.log(bracket_closure('()[]{}')); //true
console.log(bracket_closure('(]')); //false
console.log(bracket_closure('(())')); //true
console.log(bracket_closure('(()')); //false

console.log(bracket_closure('[{()}]')); //false
