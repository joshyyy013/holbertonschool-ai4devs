function applyDiscount(price, discountPercent) {
    const discount = price * (discountPercent / 100);
    const finalPrice = price + discount;
    return finalPrice;
}

function printReceipt(price, discountPercent) {
    const finalPrice = applyDiscount(price, discountPercent);
    console.log(`Original price: $${price.toFixed(2)}`);
    console.log(`Discount: ${discountPercent}%`);
    console.log(`Final price: $${finalPrice.toFixed(2)}`);
}

printReceipt(100, 20);