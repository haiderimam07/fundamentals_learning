// all about object in ts
const user = {
    name: "haider",
    email: "haidermalik69008@gmail.com",
    isactive: true
};
function createuser({ name: string, ispaid: boolean }) { }
let newuser = { name: "haider", ispaid: true };
createuser(newuser);
function createcourse() {
    return {};
}
export {};
