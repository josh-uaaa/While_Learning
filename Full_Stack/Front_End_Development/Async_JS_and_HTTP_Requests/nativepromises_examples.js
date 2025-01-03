// Constructing a Promise Object.
const inventory = {
    sunglasses: 1900,
    pants: 1088,
    bags: 1344
};

function myExecutor(resolve, reject) {
    if (inventory.sunglasses > 0) {
        resolve('Sunglasses order processed.');
    } else {
        reject('That item is sold out.');
    }
}

function orderSunglasses() {
    return new Promise(myExecutor);
}

const orderPromise = orderSunglasses();
console.log(orderPromise);

// setTimeout() Function.
console.log("This is the first line of code in app.js.");

function usingSTO() {
    console.log('I love basketball.');
}
setTimeout(usingSTO, 3000);

console.log("This is the last line of code in app.js.");

// Success and Failure Callback Functions.
import { checkInventory } from './nativepromises_libraries.js';

const order = [['sunglasses', 1], ['bags', 2]];

function handleSuccess(resolvedValue) {
    console.log(resolvedValue);
}

function handleFailure(rejectedValue) {
    console.log(rejectedValue);
}

checkInventory(order).then(handleSuccess, handleFailure);

// Using catch() with Promises.
const handleSuccess = (resolvedValue) => {
    console.log(resolvedValue);
};

const handleFailure = (rejectReason) => {
    console.log(rejectReason);
};

checkInventory(order).then(handleSuccess).catch(handleFailure);

// Chaining Multiple Promises.
import { checkInventoryNew, processPayment, shipOrder } from './nativepromises_libraries.js';

const newOrder = {
    items: [['sunglasses', 1], ['bags', 2]],
    giftcardBalance: 79.82
};

checkInventoryNew(newOrder)
    .then((resolvedValueArray) => {
        return processPayment(resolvedValueArray);
    })
    .then((resolvedValueArray) => {
        return shipOrder(resolvedValueArray);
    })
    .then((successMessage) => {
        console.log(successMessage);
    })
    .catch((errorMessage) => {
        console.log(errorMessage);
    });

// Using Promise.all().
import { checkAvailability } from './nativepromises_libraries.js';

const onFulfill = (itemsArray) => {
    console.log(`Items checked: ${itemsArray}`);
    console.log(`Every item was available from the distributor. Placing order now.`);
};

const onReject = (rejectionReason) => {
    console.log(rejectionReason);
};

const checkSunglasses = checkAvailability('sunglasses', 'Favorite Supply Co.');
const checkPants = checkAvailability('pants', 'Favorite Supply Co.');
const checkBags = checkAvailability('bags', 'Favorite Supply Co.');

Promise.all([checkSunglasses, checkPants, checkBags])
    .then(onFulfill)
    .catch(onReject);