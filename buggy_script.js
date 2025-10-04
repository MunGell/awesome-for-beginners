// A buggy JavaScript file for testing Greptile's bug detection capabilities
// This file contains various types of bugs that should be caught

function calculateSum(numbers) {
    // Bug: No validation that numbers is an array
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}

function processUserData(user) {
    // Bug: No null/undefined checks
    if (user.name === undefined) {
        return "No name found";
    }
    
    // Bug: This will cause a TypeError if user.age is not a number
    if (user.age > 18) {
        return `${user.name} is an adult`;
    } else {
        return `${user.name} is a minor`;
    }
}

function divideNumbers(a, b) {
    // Bug: No check for division by zero
    return a / b;
}

function findMaximum(numbers) {
    // Bug: No validation that numbers is an array or not empty
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }
    return max;
}

function validateEmail(email) {
    // Bug: Very basic validation, will accept invalid emails
    return email.includes('@') && email.includes('.');
}

function fetchUserData(userId) {
    // Bug: Using deprecated XMLHttpRequest without proper error handling
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/users/${userId}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            // Bug: No check for HTTP status codes
            const userData = JSON.parse(xhr.responseText);
            return userData;
        }
    };
    xhr.send();
}

function processArray(arr) {
    // Bug: Using for...in on arrays (should use for...of or regular for loop)
    for (let index in arr) {
        console.log(arr[index]);
    }
}

// Main execution with various buggy operations
const testData = {
    name: 'John Doe'
    // Missing age field - will cause undefined access
};

// This will cause issues
const result = processUserData(testData);
console.log(result);

// This will cause division by zero
const divisionResult = divideNumbers(10, 0);
console.log(`10 / 0 = ${divisionResult}`);

// This will cause issues with undefined
const maxResult = findMaximum(undefined);
console.log(`Maximum: ${maxResult}`);

// This will accept invalid emails
const invalidEmails = ['not-an-email', 'test@', '@domain.com'];
invalidEmails.forEach(email => {
    const isValid = validateEmail(email);
    console.log(`${email} is valid: ${isValid}`);
});

// This will cause issues with for...in on arrays
const numbers = [1, 2, 3, 4, 5];
processArray(numbers);

// Bug: Using var instead of let/const (not necessarily a bug but bad practice)
var globalVariable = "This should be const or let";

// Bug: Missing semicolon (can cause issues in some cases)
const missingSemicolon = "This line is missing a semicolon"

// Bug: Unused variable
const unusedVariable = "This variable is never used";

// Bug: Function that doesn't return anything but is expected to
function getCurrentTime() {
    const now = new Date();
    // Missing return statement
}

// Bug: Async function without proper error handling
async function fetchData() {
    const response = await fetch('/api/data');
    // Bug: No check if response is ok
    const data = await response.json();
    return data;
}
