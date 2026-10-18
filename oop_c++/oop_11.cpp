// file handling in c++

#include<bits/stdc++.h>
#include<fstream>

using namespace std;




int main(){

    // to write we createed fout object
    ofstream fout;

    // opening of file
    fout.open("zoom.txt");
    fout<<"hello haider this is ai";
    // closing of file it isnecessary as opening of file use resource it takes the persisted data into memory and perform tasks 
    fout.close();


    // to read the fle
    ifstream fin;
    fin.open("zoom.txt");

    char c;
    c=fin.get();
    
    while(!fin.eof()){
        cout<<c;
        c=fin.get();

    }
    fin.close();

}