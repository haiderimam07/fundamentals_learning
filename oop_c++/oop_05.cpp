#include<bits/stdc++.h>
using namespace std;

// inheritance in oop
// the capacity of a class to derive property and characteristics from another class


// public, private and protected 
// public: access everywhere
// private:access only within class
// protected: access only in derived class(child)
// note: it does not matter what is the acess modifuer is but within class everything si accessible
class Human{
    protected:
        string name;
        int age, weight;

    
    public:
        Human(string name, int age, int weight){
            this->name=name;
            this->age=age;
            this->weight=weight;
        }
        void update_weight(int weight){
            this->weight=weight;
        }
        void update_age(int age){
            this->age=age;
        }
        void display(){
            cout<< name <<" "<< age <<" "<<weight<<endl;
        }


};

// as student and teacher both are human so we can use poperty of human in the student and teacher 
// hence human as the parent class and student and teacher as the child class 
// here protected means whatever this class inhertied will be protected but it will depend upon the priority private>protected>public

// for eg if the class property is defined as the protected in the parent class but we inherit that calss as the public it would still copy that property in the protected becasue priority of proected is higher 
// 2 eg if the property in the parent class is defined as public but we inherit as the private or protected means that property wouldonly be accessible inside the child class even if the property in the parent class is defined as the public 


class Student: public Human{
    private:
        int roll_num, fees;

    public:
        Student(string name, int age, int weight, int roll_num, int fees): Human (name, age ,weight){
            this->roll_num=roll_num;
            this->fees=fees;
        }
        void display(){
            cout<<name <<endl<<age <<endl<<weight<<endl<<roll_num <<endl<<fees<<"\n";
        }


};

class Teacher: public Human{
    private:
        int id , salary;

    public:
        Teacher(string name, int age, int weight, int id, int salary):Human(name, age, weight){
            this->id=id;
            this->salary=salary;
        }

};


int main(){
    // let first create humna object
    Human h1("haider", 24, 60);
    h1.display();  
    
    Student s1("amit", 23, 67, 2708, 3000);
    s1.display();
    s1.update_weight(90);
    s1.display();



}