#include<bits/stdc++.h>
using namespace std;



class Customer{
    private:
        string name;
        int account, balance;
    public:
        Customer(string name, int account, int balance){
            this->name=name;
            this->account=account;
            this->balance=balance;
        }
        
        void credit(int amount){
            if (amount<0) throw "amount is less than zero";
            // if error is thrown then nothing will exceute under that
            balance+=amount;
            cout<<amount <<" is credited"<<endl;
            
        }

        void debit(int amount){
            if(amount>0 && balance>=amount){
                balance-=amount;
                cout<<amount <<"is debited"<<endl;
            }
            else if(amount<0){
                throw "is less than zero";

            }
            else{
                throw "balance is low";
            }
        }
};
// ls
// exception handling in c++
int main(){
    Customer c1("haider", 1, 5000);
    try{

        c1.credit(5000);
        c1.debit(90000);
        c1.credit(70000);
    }catch(const char *e){
        cout<<"exception occured" <<e<<endl;
    }
}