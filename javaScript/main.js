// everything in the js to learn will be here in the sequence 


// 1. variables declaration three method let, const and var 
// let is the new way and nearly use everywhere and var is the old way 
// const is same as let just you cannot reassign const 

let curUserName='haider';
curUserName= 'Imam';

console.log(curUserName);

const userName ='Haider';
userName='Imam';
console.log(userName); //it'll give type error

// note: let and const both are block scope variable but var is not once var is declared it will be declared undefined until the value isnot assigned to the variable 

// Here is a point-by-point summary of hoisting in JavaScript:

// 1. Definition: Hoisting is the JavaScript engine's behavior of moving declarations to the top of their scope during the compilation phase before code execution.

// 2. Declarations vs. Initializations: Only declarations are hoisted; assignments and initial values stay exactly where they are written in the code.

// 3. Function Declarations: Fully hoisted along with their body, allowing you to invoke them before their actual line of definition in the code.

// 4. Function Expressions: Not hoisted as functions; they inherit the hoisting behavior of the variable type (var, let, or const) they are assigned to.

// 5. var Variables: Hoisted to the top of their scope and automatically initialized with a value of undefined, meaning accessing them early returns undefined rather than crashing.

// 6. let and const Variables: Hoisted to the top of their block scope, but not initialized with any value.

// 7. Temporal Dead Zone (TDZ): The execution zone from the start of a block until a let or const variable is declared, during which accessing the variable throws a ReferenceError.


const accountId =1234566;
let gmailId='haider@gmail.com';
var password='haider@124';

console.table([accountId,gmailId,password]);

