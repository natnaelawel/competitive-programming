function triangle(number) {
  for (let i = 1; i <= number; i++) {
    line = "";
    for (let hash = 1; hash <= i ; hash++) {
      line += "*";
    }
    console.log(`${line}`);
  }
}
triangle(5);
