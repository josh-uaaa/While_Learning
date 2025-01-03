// The await Operator.
const brainstormDinner = () => {
    return new Promise((resolve, reject) => {
        console.log(`I have to decide what's for dinner...`)
        setTimeout(() => {
            console.log('Should I make salad...?');
            setTimeout(() => {
                console.log('Should I make ramen...?');
                setTimeout(() => {
                    console.log('Should I make eggs...?');
                    setTimeout(() => {
                        console.log('Should I make chicken...?');
                        resolve('beans');
                    }, 1000);
                }, 1000);
            }, 1000);
        }, 1000);
    });
};

// Handling Dependent Promises.
const shopForBeans = () => {
    return new Promise((resolve, reject) => {
        const beanTypes = ['kidney', 'fava', 'pinto', 'black', 'garbanzo'];
        setTimeout(() => {
            let randomIndex = Math.floor(Math.random() * 5);
            let beanType = beanTypes[randomIndex];
            console.log(`I bought ${beanType} beans because they were on sale.`);
            resolve(beanType);
        }, 1000)
    })
}

let soakTheBeans = (beanType) => {
    return new Promise((resolve, reject) => {
        console.log('Time to soak the beans.');
        setTimeout(() => {
            console.log(`... The ${beanType} beans are softened.`);
            resolve(true);
        }, 1000);
    });
}

let cookTheBeans = (isSoftened) => {
    return new Promise((resolve, reject) => {
        console.log('Time to cook the beans.');
        setTimeout(() => {
            if (isSoftened) {
                console.log('... The beans are cooked!');
                resolve('\n\nDinner is served!');
            }
        }, 1000);
    });
}

// Handling Errors.
let randomSuccess = () => {
    let num = Math.random();
    if (num < .5) {
        return true;
    } else {
        return false;
    }
};

let cookBeanSouffle = () => {
    return new Promise((resolve, reject) => {
        console.log('Fingers crossed... Putting the Bean Souffle in the oven');
        setTimeout(() => {
            let success = randomSuccess();
            if (success) {
                resolve('Bean Souffle');
            } else {
                reject('Dinner is ruined!');
            }
        }, 1000);
    });
};

// Handling Independent Promises.
let cookBeans = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('beans');
        }, 1000);
    });
}

let steamBroccoli = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('broccoli');
        }, 1000);
    });
}

let cookRice = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('rice');
        }, 1000);
    });
}

let bakeChicken = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('chicken');
        }, 1000);
    });
}

export default { brainstormDinner, shopForBeans, soakTheBeans, cookTheBeans, cookBeanSouffle, cookBeans, steamBroccoli, cookRice, bakeChicken };