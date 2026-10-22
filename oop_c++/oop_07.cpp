
#include<bits/stdc++.h>
using namespace std;


class Human{
    protected:
        string name;
        int age, weight;

    
    public:
        // Human(){}
        Human(string name){
            this->name=name;
            this->age=0;
            this->weight=0;
        }
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


class Engineer: public virtual Human{
    protected:
        string specialization;

    public:
        Engineer(string name, string specialization):Human(name) {
            this->specialization=specialization;
        }
};

class Youtuber: public virtual Human{
    protected:
        int subscribers;
    public:
        Youtuber(string name, int subscribers):Human(name) {
            this->subscribers=subscribers;
        }
        void display(){
            cout<<name<<" "<<subscribers<<endl;
        }
};

class CodeTeacher: public Engineer, public Youtuber{
    protected:
        string channel_name;
    public:
        CodeTeacher(string name, string specialization, int subscribers, string channel_name): Human(name), Engineer(name, specialization), Youtuber(name, subscribers){
            this->channel_name=channel_name;
        }

        void display(){
            cout<<name<<endl<<specialization<<endl<<subscribers<<endl<<channel_name<<endl;
        }
};




int main(){
    CodeTeacher c1("haider", "ece", 32, "coderarmy");
    c1.display();
    cout<<endl;
    Youtuber y1("imam", 45);
    y1.display();
}