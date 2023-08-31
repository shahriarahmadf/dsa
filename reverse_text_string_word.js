function reverse_text_string_word(text){
    let end = text.length;
    let reversed_text = '';
    
    for (let i=text.length-1; i >= 0; i--){
        if (text[i] == ' '){
            for (let j=i+1; j<end; j++){
                reversed_text += text[j];
            }
            reversed_text += ' ';
            end = i;
        }
    }

    if (end!= text.length){
        for (let j=0; j<end; j++){
            console.log(reversed_text);

            reversed_text += text[j];
        }
    }
    return reversed_text;
}
console.log(reverse_text_string_word('Who are you fahim'));