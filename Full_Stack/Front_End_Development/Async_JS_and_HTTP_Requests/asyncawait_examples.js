// The await Operator.
import brainstormDinner from './asyncawait_libraries.js';

function nativePromiseDinner() {
    brainstormDinner().then((meal) => {
        console.log(`I'm going to make ${meal} for dinner.`);
    });
}

async function announceDinner() {
    let meal = await brainstormDinner();
    console.log(`I'm going to make ${meal} for dinner.`);
}

announceDinner();

// Handling Dependent Promises.
import { shopForBeans, soakTheBeans, cookTheBeans } from './asyncawait_libraries.js';

async function makeBeans() {
    let type = await shopForBeans();
    let isSoft = await soakTheBeans(type);
    let dinner = await cookTheBeans(isSoft);
    console.log(dinner);
}

makeBeans();

// Handling Errors.
import { cookBeanSouffle } from './asyncawait_libraries.js';

async function hostDinnerParty() {
    try {
        let resolvedValue = await cookBeanSouffle();
        console.log(`${resolvedValue} is served!`);
    } catch (error) {
        console.log(error);
        console.log('Ordering a pizza!');
    }
}

hostDinnerParty();

// Handling Independent Promises.
import { cookBeans, steamBroccoli, cookRice, bakeChicken } from './asyncawait_libraries.js';

async function serveDinner() {
    let vegetablePromise = steamBroccoli();
    let starchPromise = cookRice();
    let proteinPromise = bakeChicken();
    let sidePromise = cookBeans();

    console.log(`Dinner is served. We're having ${await vegetablePromise}, ${await starchPromise}, ${await proteinPromise}, and ${await sidePromise}.`);
}

serveDinner();

// Await Promise.all().
async function serveDinnerAgain() {
    let foodArray = await Promise.all([steamBroccoli(), cookRice(), bakeChicken(), cookBeans()]);
    console.log(`Dinner is served. We're having ${foodArray[0]}, ${foodArray[1]}, ${foodArray[2]}, and ${foodArray[3]}.`);
}

serveDinnerAgain();