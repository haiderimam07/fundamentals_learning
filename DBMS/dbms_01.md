 <!-- this is what i have for the commit to be done in order to check do they track it correctt or not -->
 <!-- this is for the wsl commit in order to check weather it is working fine ro  not -->
 <!-- check bash commit -->

 <!-- check wsl commit -->


 <!-- bash commit test-3 -->
 <!-- wsl commit test 3 -->

 <!-- bash commit test 4 -->

 <!-- wsl commit test 4 -->

 <!-- bash test5  -->
 <!-- bash test 5 -->
 ```c++

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
 ```

 ```python
 print("hello world")
```


```javascript
function addtwo(num) {
    return num + 2;
}
function getupper(val) {
    return val.toUpperCase();
}
```