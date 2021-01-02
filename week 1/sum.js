function sumPostive(number1, number2) {
  let [greater, smaller] =
    number1.length > number2.length ? [number1, number2] : [number2, number1];
  let result = "";
  let carry = 0;
  let digitDif = greater.length - smaller.length;
  for (let k = 0; k < digitDif; k++) {
      smaller = "0" + smaller;
  }
  console.log(smaller, " is smaller");
  for (var i = smaller.length - 1; i >= 0; i--) {
    sum = parseInt(greater[i]) + parseInt(smaller[i]) + carry;
    if (sum > 9 && sum % 10) {
      carry = parseInt(sum / 10);
    }
    if (i === 0 && carry) {
      result = `${carry}${sum % 10}` + result;
      console.log(result, " is result");
    } else {
      result = `${sum % 10}` + result;
    }
  }
  return result;
}
console.log(sumPostive("99209", "803"));
console.log(sumPostive("61700", "7404"));
