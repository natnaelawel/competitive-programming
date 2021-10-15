
function division(number1, number2) {
    isNegative = false;
    if (number1[0] === "-" || number2[0] === "-") {
        isNegative = true;
    }
    if (number1[0] === "-" && number2[0] === "-") {
        isNegative = false;
    }
    if (number1[0] === "-") {
        number1 = number1.slice(1);
    }
    if (number2[0] === "-") {
        number2 = number2.slice(1);

    }
    if (number2 === "0") {
        console.log("Divisible by zero error")
        return null
    }
    let [upper, lower] = getUpperAndLower(number1, number2)
    let resolved = false
    let quotient = "";
    let afterPoint = 0;
    let pointIndex = 0;
    let dividendLength;
    let dividend;
    let remaining;
    while (!resolved) {
        dividendLength = ((upper.length === lower.length) ) ? (lower.length) : (lower.length + 1)
        dividend = upper.substring(0, dividendLength)
        remaining = upper.substring(dividendLength, upper.length)
        let innerQuotient = 0;
        let rem = 0;

        while (isGreater(dividend, lower)) {
            if (dividend.length === lower.length && parseInt(dividend[0]) < parseInt(lower[0])) {
                break
            }
            dividend = sumNegative(dividend, lower)
            rem = dividend
            innerQuotient++
            if (dividend[0] === "-") {
                break
            }
        }
        upper = rem + remaining
        let canDivide = isGreater(upper, lower)
        if (innerQuotient >= 10) {
            for(let i = 0; i < upper.length; i++){
                if(upper[i] === "0"){
                    innerQuotient += "0"
                    pointIndex++
                }else{
                    break
                }
            }
            pointIndex++
        }
        quotient += innerQuotient

        if (afterPoint === 0) {
            pointIndex++
        }
        if (upper !== "0" && !canDivide && afterPoint < 10) {
            while (!isGreater(upper, lower)) {
                upper = upper + "0"
                if (!isGreater(upper, lower)) {
                    quotient += "0"
                }
            }
            afterPoint++
        }
        if (upper === "0" || afterPoint === 5) {
            resolved = true
        }
    }
    quotient = quotient.slice(0, pointIndex) + "." + quotient.slice(pointIndex, quotient.length)
    return isNegative ? -1 * quotient : quotient
}

console.log(division("100", "4"))
console.log(division("123404", "1234"))
console.log(division("12345", "1234"))
console.log(division("12001021021021021021", "156423453"))

function sumNegative(number1, number2) {
    let [upper, lower] = getUpperAndLower(number1, number2)
    if (upper === lower) {
        return "0"
    }
    let result = "";
    let carry = 0;
    let digitDif = upper.length - lower.length;
    for (let k = 0; k < digitDif; k++) {
        lower = "0" + lower;
    }
    let isNegative = false;
    if (upper.length === lower.length && parseInt(upper[0]) < parseInt(lower[0])) {
        isNegative = true
    }
    for (var i = lower.length - 1; i >= 0; i--) {
        let upperValue = parseInt(upper[i]) - carry;
        let lowerValue = parseInt(lower[i]);
        if (upperValue >= lowerValue) {
            sum = upperValue - lowerValue;
            carry = 0;
        } else {
            sum = 10 + upperValue - lowerValue;
            carry = 1;
        }

        result = `${sum % 10}` + result;
    }

    resultLength = result.length;
    updatedResult = result
    for (let j = 0; j <= resultLength; j++) {
        if (result[j] === "0") {
            updatedResult = result.slice(1);
        } else {
            break;
        }
    }
    result = result.replace(/^0+/, '');
    return isNegative ? '-' + result : result;
}


function isGreater(number1, number2) {
    if (number1.length > number2.length) {
        return true
    } else if (number1.length < number2.length) {
        return false
    }
    else {
        for (let i = 0; i < number1.length - 1; i++) {
            let num1 = parseInt(number1[i])
            let num2 = parseInt(number2[i])
            if (num1 > num2) {
                return true
            } else if (num1 < num2) {
                return false
            }
        }
        return true
    }
}
function getUpperAndLower(number1, number2) {
    return isGreater(number1, number2) ? [number1, number2] : [number2, number1];
}
