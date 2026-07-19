#include <bits/stdc++.h>
#define ll long long

const ll INF = 2e18;

using namespace std;

int main() {
    int n; cin >> n;

    vector<ll> dura(n);
    for (int i=0; i<n; i++){
        cin >> dura[i];
    }

    ll ans = INF;

    for (int i=0; i<n-1; i++){
        ll x = dura[i], y = dura[i+1];
        if (x < y) swap(x, y);

        ans = min(ans, max((x+1)/2, (x+y+2)/3));
    }

    for (int i=0; i<n-2; i++){
        ll x = dura[i], y = dura[i+2];

        ans = min(ans, (x+y+1)/2);
    }

    sort(dura.begin(), dura.end());
    long long current = (dura[0] + 1) / 2 + (dura[1] + 1) / 2;
    ans = min(ans, current);

    cout << ans << endl;
    return 0;
}