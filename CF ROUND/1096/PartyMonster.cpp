#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void sol(){
    int n; cin >> n;
    string s; cin >> s;

    int l=0, r=0; 
    for(int i=0; i<n; i++){
        if(s[i] == '('){
            l++;
        } else {
            r++;
        }
    }

    if(r==l){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main(){
    int tc; cin >> tc;
    while(tc--) sol();
    return 0;
}
