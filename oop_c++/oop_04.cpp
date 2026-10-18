// static data member
// static member function
// created by static keyword

// Encapsulation: wrapping up of the data and info in a single unit, while controlling access to them

// abstraction:Displaying only essential info and hiding the details

#include<bits/stdc++.h>
using namespace std;

class customer{
    private:
        string name;
        int account, balance;
        static int total_customer;
        
    
    public:
        // static int total_customer;
        // constructor
        customer(string name, int account, int balance){
            this->name=name;
            this->account=account;
            this->balance=balance;
            total_customer++;
        }
        customer(string name, int account){
            this->name=name;
            this->account=account;
            this->balance=0;
            total_customer++;
        }

        // return total customer; this is the static member function it can access static data which is private
        static int total_Customer(){
            return total_customer;
        }

};

int customer::total_customer=0;


int main(){
    customer a1("rohit", 1, 1000);
    customer a2("haider", 2, 1400 );
    customer a3("anil", 3, 4000);
    
    int total=a1.total_Customer();
    cout<<total<<endl;
    // we can access our total customer without the help of the object as it belong to the class
    // and we can do this by this syntax 

    // :: this is class resolution
    // int tot=customer::total_customer;
    // cout<<tot;

    // here we are accessing the static data member by static memeber function and this is the syntax for it 
    int tot=customer::total_Customer();
    cout<<tot;


}