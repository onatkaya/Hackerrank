#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int n,q;
    
    cin >> n >> q;
    
    vector<vector<int>> main_vec;
    
    // inserting elements part
    
    for(int i = 0; i < n; i++){
        
        int temp_size;
        
        cin >> temp_size;
        
        vector<int> temp_vec;
        
        for(int j = 0; j < temp_size; j++){
            int temp_element;
            
            cin >> temp_element;
            
            temp_vec.push_back(temp_element);    
        
            
        }
        
        main_vec.push_back(temp_vec);
        temp_vec.clear();
        
        
    }
    
    // printing elements part
    
    for(int i = 0; i < q; i++){
        
        int temp_index, temp_element;
        
        cin >> temp_index >> temp_element;
        
        cout << main_vec[temp_index][temp_element] << endl;
        
    }
    
    return 0;
}
