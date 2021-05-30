#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int n;

    cin >> n;

    vector<int> result;

    int num;

    for (int i = 0; i < n; i++)
    {
        cin >> num;
        result.push_back(num);
    }

    sort(result.begin(), result.end());

    for (int x : result)
        cout << x << " ";

    return 0;
}
