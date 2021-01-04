function twoStacks(x, a, b) {
    let lengthB = 0;
    let sum = 0;
    while (lengthB < b.length && sum + b[lengthB] <= x) {
        sum += b[lengthB];
        lengthB++;
    }

    let maxScore = lengthB;
    for (let lengthA = 1; lengthA <= a.length; lengthA++) {
        sum += a[lengthA - 1];

        while (sum > x && lengthB > 0) {
            lengthB--;
            sum -= b[lengthB];
        }

        if (sum > x) {
            break;
        }

        maxScore = Math.max(maxScore, lengthA + lengthB);
    }
    return maxScore;
}