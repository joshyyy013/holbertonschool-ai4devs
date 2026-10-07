function sumNumbers(numbers) {
    let total = 0;
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}

function main() {
    const numbers = [2, 4, 6, 8];
    const total = sumNumbers(numbers);
    console.log(`Numbers: ${numbers.join(", ")}`);
    console.log(`Total: ${total}`);
}

main();