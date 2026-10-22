// type of inheritance

// single inheritance
// a class is allowed to inherit from only one class


// multilevel inheritance
// person->employee->manager 
// 


// multiple Inheritance-inherit mulitple parent class
// 


#include<bits/stdc++.h>
using namespace std;

// single inheritance it can also be view as the hierarchal inheritance as student and teahcer both are inheriting theproperty of the humna
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

// multilevel inheritacne
class Person{
    protected:
        string name;

    public:
        Person(string name){
            this->name=name;
        }

};

class Employee: public Person{
    protected:
        int salary;

    public:
        Employee(string name, int salary): Person(name){
            this->salary=salary;
        }
};

class Manager:public Employee{
    protected:
        string department;
    public:
        Manager(string name, int salary, string department):Employee(name, salary){
            this->department=department;
        }
        void display(){
            cout<<name <<endl<<salary<<endl<<department<<endl;
        }
};


// multiple inheritance

class Engineer{
    protected:
        string specialization;

    public:
        Engineer(string specialization){
            this->specialization=specialization;
        }
};

class Youtuber{
    protected:
        int subscribers;
    public:
        Youtuber(int subscribers){
            this->subscribers=subscribers;
        }
};

class CodeTeacher: public Engineer, public Youtuber{
    protected:
        string name;
    public:
        CodeTeacher(string name, string specialization, int subscribers):Engineer(specialization), Youtuber(subscribers){
            this->name=name;
        }

        void display(){
            cout<<specialization<<endl<<subscribers<<endl<<name<<endl;
        }
};

// hierarchal inheritance

// single base class property can be inherited by multiple derivative classes same as the tree datastrucutre


// hybrid inheritance
// mix of above all nultilevel+ mulitple +hierarchal


// multipath inheritance
//  human->engineer ->\ Codeteacher    codeteacher is inheriting the humna calss form two diffrent path 
//      |->youtuber ->/

// if human class  have name and age then codeteacher would inherit them twice once from the engineer and other fro the youtuber let see how to handle this situaiton in the oop_07.cpp file





int main(){
    Manager m1("haider",899, "HR");
    m1.display();


    CodeTeacher c1("haider", "ece",100);
    c1.display();
}