// A buggy TypeScript file for testing Greptile's bug detection capabilities
// This file contains various type-related bugs that should be caught

interface User {
    name: string;
    age: number;
    email: string;
}

interface Config {
    apiUrl: string;
    timeout: number;
    retries: number;
}

function calculateSum(numbers: number[]): number {
    // Bug: No validation that numbers is not empty
    let total = 0;
    for (const num of numbers) {
        total += num;
    }
    return total;
}

function processUserData(user: User): string {
    // Bug: No null/undefined checks despite TypeScript types
    if (user.name === undefined) {
        return "No name found";
    }
    
    if (user.age > 18) {
        return `${user.name} is an adult`;
    } else {
        return `${user.name} is a minor`;
    }
}

function divideNumbers(a: number, b: number): number {
    // Bug: No check for division by zero
    return a / b;
}

function findMaximum(numbers: number[]): number {
    // Bug: No validation that numbers is not empty
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }
    return max;
}

function validateEmail(email: string): boolean {
    // Bug: Very basic validation, will accept invalid emails
    return email.includes('@') && email.includes('.');
}

// Bug: Function with wrong return type annotation
function getCurrentTime(): string {
    const now = new Date();
    return now.getTime(); // Bug: Returns number but annotated as string
}

// Bug: Function with missing return type annotation
function processConfig(config: Config) {
    // Bug: No return statement but function might be expected to return something
    console.log(`API URL: ${config.apiUrl}`);
}

// Bug: Async function without proper error handling
async function fetchUserData(userId: number): Promise<User> {
    const response = await fetch(`/api/users/${userId}`);
    // Bug: No check if response is ok
    const userData = await response.json();
    return userData; // Bug: userData might not match User interface
}

// Bug: Function with incorrect parameter types
function concatenateStrings(str1: string, str2: number): string {
    return str1 + str2; // Bug: str2 is number but being concatenated as string
}

// Bug: Interface with optional properties that are used as required
interface Product {
    id?: number;
    name?: string;
    price?: number;
}

function displayProduct(product: Product): string {
    // Bug: Using optional properties as if they're required
    return `Product ${product.id}: ${product.name} - $${product.price}`;
}

// Bug: Generic function with incorrect type constraints
function getFirstItem<T extends string>(items: T[]): T {
    return items[0]; // Bug: No check if array is empty
}

// Bug: Class with incorrect property types
class UserManager {
    private users: User[] = [];
    
    addUser(user: User): void {
        this.users.push(user);
    }
    
    getUserById(id: number): User {
        // Bug: No validation that user exists
        return this.users.find(user => user.id === id); // Bug: User interface doesn't have id property
    }
    
    getUsersCount(): string {
        // Bug: Returns number but annotated as string
        return this.users.length;
    }
}

// Bug: Enum with duplicate values
enum Status {
    PENDING = 'pending',
    APPROVED = 'approved',
    REJECTED = 'rejected',
    PENDING = 'pending' // Bug: Duplicate value
}

// Bug: Type assertion without proper validation
function processApiResponse(response: any): User {
    // Bug: Unsafe type assertion
    return response as User;
}

// Bug: Function with incorrect overloads
function formatValue(value: string): string;
function formatValue(value: number): string;
function formatValue(value: string | number): string {
    if (typeof value === 'string') {
        return value.toUpperCase();
    } else {
        return value.toString();
    }
}

// Bug: Missing return type in arrow function
const processData = (data: any) => {
    // Bug: No return type annotation
    return JSON.stringify(data);
};

// Bug: Incorrect use of readonly
interface ReadonlyUser {
    readonly name: string;
    readonly age: number;
}

function updateUser(user: ReadonlyUser): void {
    // Bug: Trying to modify readonly property
    user.name = 'Updated Name';
}

// Main execution with various buggy operations
const testUser: User = {
    name: 'John Doe',
    age: 25,
    email: 'john@example.com'
};

// This will work but has type issues
const result = processUserData(testUser);
console.log(result);

// This will cause division by zero
const divisionResult = divideNumbers(10, 0);
console.log(`10 / 0 = ${divisionResult}`);

// This will cause issues with empty array
const maxResult = findMaximum([]);
console.log(`Maximum: ${maxResult}`);

// This will cause type issues
const timeResult = getCurrentTime();
console.log(`Current time: ${timeResult}`);

// This will cause type issues
const concatResult = concatenateStrings('Hello', 123);
console.log(`Concatenated: ${concatResult}`);

// This will cause issues with optional properties
const product: Product = {};
const productDisplay = displayProduct(product);
console.log(productDisplay);

// This will cause issues with readonly properties
const readonlyUser: ReadonlyUser = { name: 'Jane', age: 30 };
updateUser(readonlyUser);
