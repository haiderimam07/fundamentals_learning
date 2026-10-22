#include<bits/stdc++.h>
using namespace std;

class customer{
    string name;
    int account;
    int balance;


    // this is constructor we can have multipl constructor
    public:
        customer(string name, int account, int balance){
            this->name=name;
            this->account=account;
            this->balance=balance;
        }
        // inline constructor
        inline customer(string a, int b): name(a), account(b){}

        // copy cunstructor it is already present hiddden we do not have to write it manually but here is an example
        customer(customer &b){
            name=b.name;
            account=b.account;
            balance=b.balance;
        }

        // destructor
        // ~customer(){

        // }



};




int main(){
    // customer c1=customer("haider", 43,2);

}