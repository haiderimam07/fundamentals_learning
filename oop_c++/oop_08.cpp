// polymorphism
// it means many forms means samename but exist in different forms 

#include<bits/stdc++.h>
using namespace std;


// here same name function exist which is function overload but it can exist simulataneously bcs of different paramaters

// function overload polymorphism
class Area{
    public:
        int calculate_area(int r){
            return 3.14*r*r;
        }
        int calculate_area(int length, int breadth){
            return length* breadth;
        }

};

// operator overload polymorphism
class Complex{
    int real, img;
    public:
        Complex(){}
        Complex(int real, int img){
            this->real=real;
            this->img=img;
        }
        void display(){
            cout<<real<<"+ i"<<img<<endl;
        }
        Complex sum(Complex c1, Complex c2){
            Complex c3;
            c3.real=c1.real+c2.real;
            c3.img=c1.img+c2.img;
        }
        Complex operator +(Complex &c){
            Complex ans;
            ans.real=real+c.real;
            ans.img=img+c.img;
            return ans;
        }

};

// virtual functions
class Animal{
    public:
        virtual void speak(){
            cout<<"huhu";
        }

};

class Dog: public Animal{
    public:
        void speak(){
            cout<<"bhow";
        }

};




int main(){
    Complex f(2,3);
    Complex s(3,7);
    Complex t=f+s; //f+s menas here like this f.func(s) that is why only one is in the argument of the operator fucntion
    //t.sum(f,s);
    f.display();
    s.display();
    t.display();
    //virtual funciton
    Animal *p;
    p=new Dog();
    // if the virtual is not there before animal speak() then p->speak will execute huhu but when we write virtual then it says do not decide at the compile time only run at the runtime hence when runtime happen then it checkswhich object address is save in the pointer then ti will point to that object
    p->speak();

}