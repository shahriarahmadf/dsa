/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    let anagram_index = [];

    // anagram checker function
    const checkAnagram = (p_dict,s_window_dict, anagram_index, position) => {
        let temp = true;
        const p_keys = Object.keys(p_dict);
        const s_keys = Object.keys(s_window_dict);
        if(p_keys.length == s_keys.length){
            for (const key of p_keys){
                if (p_dict[key] !== s_window_dict[key]){
                    continue;
                    temp = false;
                }
            }
            if(temp == true){
                anagram_index = [...anagram_index,position];
                        }
        }
        console.log(anagram_index);
        return anagram_index;
    }

    if (s.length < p.length){
        return anagram_index;
    }

    // finding small string/p map
    p_dict = {};
    for (const letter of p){
        if (p_dict[letter]){
            p_dict[letter]++;
        }
        else{
            p_dict[letter] = 1;
        }
    }

    // window sliding
    s_window_dict = {}
    // base case
    for (let i=0; i<p.length; i++){
        if (s_window_dict[p[i]]){
            s_window_dict[p[i]]++;
        }
        else{
            s_window_dict[p[i]] = 1;
        }
    }
    // if anagram for base case
    anagram_index = checkAnagram(p_dict,s_window_dict,anagram_index,0);

    // window slider cases
    for (let i=1; i< s.length-p.length + 1; i++){

        // deleting left char
        const left_char = s[i-1];
        s_window_dict[left_char]--;

        if (s_window_dict[left_char]==0){
            delete s_window_dict.left_char;
        }       

        // adding right char
        const right_char = s[i+p.length-1];
        if (s_window_dict[right_char]){
            s_window_dict[right_char]++;
        }
        else{
            s_window_dict[right_char] = 0;
        }

        // if anagram for window slider cases
        anagram_index = checkAnagram(p_dict,s_window_dict,anagram_index,i);
    }

};

console.log(findAnagrams('cbaebabacd','abc'));