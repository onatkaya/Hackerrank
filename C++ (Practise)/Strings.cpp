#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
  
    string str1, str2;
    
    cin >> str1;
    
    cin >> str2;
    
    cout << str1.size() << " " << str2.size() << endl;
    
    cout << str1 + str2 << endl;
    
    cout << str2[0] + str1.substr(1) << " " << str1[0] + str2.substr(1) << endl;
    
    return 0;
}