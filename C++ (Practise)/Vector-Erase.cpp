#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    vector<int> result;
    int n;
    
    cin >> n;
    
    int num;
    
    for(int i = 0; i < n; i++)
    {
        cin >> num;
        result.push_back(num);
    }
    
    int pos1;
    cin >> pos1;
    
    result.erase(result.begin()+pos1-1);
    
    int range1, range2;
    cin >> range1 >> range2;
    
    result.erase(result.begin()+range1-1, result.begin()+range2-1);
    
    cout << result.size() << endl;
    
    for(int x: result)
        cout << x << " ";
      
    return 0;
}
