function triangle(number) {
  for (let i = 0; i < number; i++) {
    line = "";
    for (let space = number - i; space > 0; space--) {
      line += " ";
    }
    for (let hash = 0; hash <= 2 * i; hash++) {
      line += "*";
    }

    console.log(`${line}`);
  }
}
triangle(5);
