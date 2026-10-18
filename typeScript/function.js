// this will nly take the num as the number
function addtwo(num) {
    return num + 2;
}
function getupper(val) {
    return val.toUpperCase();
}
getupper("haider");
function signUpUser(name, email, password, ispaid) {
    // 
}
// arrow function
// in this boolean false is default values so even if we do not provide in the function call it will not throw error
let loginuser = (name, email, ispaid = false) => {
};
// function should also have what type they will return
// now if we return anything else it will throw error
function addtw(num) {
    return num + 2;
}
const gethello = (s, k) => {
    return "";
};
const heros = ["thor", "marvel", "iron man", "spider man"];
heros.map((hero) => {
    return `hero is ${hero}`;
});
// some function does not return a value we infer that by void type 
function consoleError(errmsg) {
    console.log(errmsg);
}
// 
function hanldeError(msg) {
    throw new Error(msg);
}
export {};
