#include<bits/stdc++.h>
using namespace std;




int main(){

    try{
        int *p=new int[10000];
        cout<<"ememory allocation suddecful";
        delete []p;
    }catch(const exception &e){
        cout<<"error occured:"<<e.what();
    }
}
