/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length){
        return false;
    }
    let s_dict = {};
    let t_dict = {};

    for (let char=97; char <= 122; char++){
        const character = String.fromCharCode(char);
        s_dict[character] = 0;
        t_dict[character] = 0;
    }

    for (let i=0; i<s.length; i++){
        s_dict[s[i]] += 1;
        t_dict[t[i]] += 1;
    }

    const s_values = Object. values(s_dict);
    const t_values = Object.values(t_dict);

    for (i=0; i<s_values.length; i++){
        if (s_values[i] != t_values[i]){
            return false;
        }
    }
    return true;

};