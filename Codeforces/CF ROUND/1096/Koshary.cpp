#include <iostream>

using namespace std;

void sol(){
    int x, y; cin >> x >> y;
    if (x%2==1 && y%2==1){
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
    }
}

int main(){
    int tc; cin >> tc;
    while(tc--) sol();
    return 0;
}
