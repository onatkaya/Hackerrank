#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

// Write your Student class here

class Student{
    
   public:
        
        int scores[5];
    
        void input()
        {
            int num_1, num_2, num_3, num_4, num_5;
            
            cin >> num_1 >> num_2 >> num_3 >> num_4 >> num_5;
            
            scores[0] = num_1;
            scores[1] = num_2;
            scores[2] = num_3;
            scores[3] = num_4;
            scores[4] = num_5;
        }
        
        int calculateTotalScore(){
            
            int result = 0;
            
            for(int x: scores){
                result += x;
            }
        
           return result; 
        }  
    
};

int main() {
    int n; // number of students
    cin >> n;
    Student *s = new Student[n]; // an array of n students
    
    for(int i = 0; i < n; i++){
        s[i].input();
    }

    // calculate kristen's score
    int kristen_score = s[0].calculateTotalScore();

    // determine how many students scored higher than kristen
    int count = 0; 
    for(int i = 1; i < n; i++){
        int total = s[i].calculateTotalScore();
        if(total > kristen_score){
            count++;
        }
    }

    // print result
    cout << count;
    
    return 0;
}
