function occurence(s, n) {
    if (s === "a") return n
    let repeatN = parseInt(n / s.length)
    let rem = n % s.length

    let count1 = 0;
    let count2 = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "a") {
            if (i < rem) {
                count1++
            }
            count2++
        }
    }
    return count1 + (count2 * repeatN)
}

console.log(occurence("gfcaaaecbg", 547602))