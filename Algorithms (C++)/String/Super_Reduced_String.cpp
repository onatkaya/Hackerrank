#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'superReducedString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string superReducedString(string s) {

    int index = 0;

    bool finished = 0;

    while (!finished)
    {
        if (s[index] == s[index + 1])
        {
            s.erase(index, 2);
            index = 0;
        }
        else
        {
            if (index == (int)s.size() - 1 or s.size() == 0)
                finished = 1;

            else
                index++;

        }
    }

    if (s.size() == 0)
        return "Empty String";

    else
        return s;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = superReducedString(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
