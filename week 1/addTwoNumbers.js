function addTwoNumber(l1, l2) {
    let [upper, lower] = l1.length > l2.length ? [l1, l2] : [l2, l1]
    let result = []
    let carry = 0;
    while (lower.length !== upper.length) {
        lower.push(0)
    }
    for (let i = 0; i < upper.length; i++) {
        let sum = upper[i] + lower[i] + carry
        if (sum >= 10) {
            carry = parseInt(sum / 10)
            sum %= 10
            result.push(sum)
        } else {
            carry = 0;
            result.push(sum)
        }
    }
    if (carry) {
        result.push(carry)
    }
    return result
}

let l1 = [0]
let l2 = [0]
// let l1 = [2, 4, 3]
// let l2 = [5, 6, 4]
// let l1 = [9, 9, 9, 9, 9, 9, 9]
// let l2 = [9, 9, 9, 9]
console.log(addTwoNumber(l1, l2))