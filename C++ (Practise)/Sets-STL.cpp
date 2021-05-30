#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int n;
    
    cin >> n;
    
    int a,b;
    
    set<int> s;
    
    for(int i = 0; i < n; i++)
    {
        cin >> a >> b;
        
        if(a == 1)
        {
            s.insert(b);  
        }
        else if(a == 2)
        {
            set<int>::iterator itr = s.find(b);
            
            if(itr != s.end())
                s.erase(b);
            
        }
        else if(a == 3)
        {
            set<int>::iterator itr = s.find(b);
            
            if(itr != s.end())
                cout << "Yes" << endl;
            else
                cout << "No" << endl;
        }    
    }
    
    
    return 0;
}



