function sumArray(n, k, ar) {
    let resultArray = []
    for (let i = 0; i < n - 1; i++) {
        for (let j = 1; j <= n - 1; j++) {
            let result = ar[i] + ar[j]
            if ((i < j) && result % k === 0) {
                resultArray.push([i, j])
            }
        }
    }
    return resultArray.length
}
console.log(sumArray(6, 3, [1, 3, 2, 6, 1, 2,]))