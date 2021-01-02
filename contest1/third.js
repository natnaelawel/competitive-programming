function occurence(s, n) {
    if (s === "a") return n
    let repeatN = parseInt(n / s.length)
    let rem = n % s.length
    console.log(repeatN, rem)
    let count1 = 0;
    let count2 = 0;
    let remStr = s.slice(s.length - rem);

    for (let i = 0; i < remStr.length; i++) {
        let charIndex = s.indexOf("a")
        if (s[i] === "a") {
            count1++
            s = s.slice(charIndex)
        }
    }
    for (let i = 0; i < s.length; i++) {
        let charIndex = s.indexOf("a")
        if (s[i] === "a") {
            count2++
            s = s.slice(charIndex)
        }
    }
    return count1 + (count2 * repeatN)
}

console.log(occurence("aba", Number.MAX_SAFE_INTEGER))