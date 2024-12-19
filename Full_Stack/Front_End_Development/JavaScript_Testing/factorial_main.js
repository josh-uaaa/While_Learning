const Calculate = {
    factorial(num) {
        if (num === 0) {
            return 0;
        }

        let result = 1;
        while (num > 0) {
            result *= num;
            num--;
        }
        return result;
    }
}

module.exports = Calculate;