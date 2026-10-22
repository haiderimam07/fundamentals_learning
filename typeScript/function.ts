

// this will nly take the num as the number
function addtwo(num: number){
    return num+2;
}


function getupper(val: string){
    return val.toUpperCase();
}

getupper("haider")


function signUpUser(name: string, email: string, password: string, ispaid: boolean){
    // 
}

// arrow function
// in this boolean false is default values so even if we do not provide in the function call it will not throw error
let loginuser=(name:string , email:string, ispaid: boolean= false) =>{

}

// function should also have what type they will return
// now if we return anything else it will throw error
function addtw(num: number): number{
    return num+2;
}

const gethello=(s: string , k: string): string=>{
    return ""
}



const heros=["thor", "marvel", "iron man", "spider man"]

heros.map( (hero) =>{
    return `hero is ${hero}`
})


// some function does not return a value we infer that by void type 
function consoleError(errmsg: string): void{
    console.log(errmsg)
}


// 
function hanldeError(msg: string): never{
    throw new Error(msg);
}

export {}