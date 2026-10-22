#include<bits/stdc++.h>

using namespace std;

class student{
    public:
        int age;
        string name;

};



int main(){
    
    student *s1= new student;
    s1->name="haider";
    s1->age=43;
    cout<<s1->name;
}