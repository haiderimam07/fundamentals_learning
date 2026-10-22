// all about object in ts


const user={
    name: "haider",
    email: "haidermalik69008@gmail.com",
    isactive: true
}

function createuser({name: string, ispaid: boolean}){}

let newuser={name:"haider", ispaid: true}
createuser(newuser)

function createcourse():{}{
    return {}
}


// basically degineing our datatype
type User= {
    readonly _id: string;
    name: string;
    email: string;
    ispaid: boolean;
    creditcard?: number
}

// function createUser(user: User): User{
//     return {name: "", email: "", ispaid: true}
// }

// createUser({name: "", email: "", ispaid: true})

type creditnumber= {
    creditnumber: number
}
type creditname={
    creditname: string
}

type creditdetails= creditnumber & creditname & {
    cvv: string;
}




export {}