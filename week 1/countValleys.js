function countingValleys(steps, path) {
    let fromSeaLevel = 0;
    let valleys = 0;

    for (let i = 0; i < steps; i++) {
        if (path[i] === "U") {
            fromSeaLevel++
        } else {
            fromSeaLevel--;
        }
        if (fromSeaLevel === 0 && path[i] === "U") {
            valleys++
        }
    }
    return valleys;

}
console.log(countingValleys(8, "UDDDUDUU"))
console.log(countingValleys(12, "DDUUDDUDUUUD"))