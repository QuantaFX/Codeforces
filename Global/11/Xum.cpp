#include <bits/stdc++.h>
#define ll long long

using namespace std;

ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll x1, y1, d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

vector<string> ops;

void add_op(char type, ll a, ll b){
    ops.push_back(to_string(a) + " " + type + " " + to_string(b));
}

ll mult(ll C, ll v){
    ll res = 0, p2 = v;
    bool first = true;
    for (int i = 0; (1LL << i) <= C; ++i) {
        if ((C >> i) & 1) {
            if (first) {
                res = p2;
                first = false;
            } else {
                add_op('+', res, p2);
                res += p2;
            }
        }
        if ((1LL << (i + 1)) <= C) {
            add_op('+', p2, p2);
            p2 += p2;
        }
    }
    return res;
}

int main() {
    ll x; cin >> x;
    ll y = 0;
    int best_k = 1;
    
    for (int k = 1; k <= 40; ++k) {
        ll cand = x ^ (x << k);
        if (gcd(x, cand) == 1) {
            y = cand;
            best_k = k;
            break;
        }
    }
    
    ll cur = x;
    for (int i = 0; i < best_k; ++i) {
        add_op('+', cur, cur);
        cur += cur;
    }
    add_op('^', x, cur);
    
    ll A0, B0;
    extgcd(x, y, A0, B0);
    
    ll A = (A0 % y + y) % y;
    if (A == 0) A += y;
    ll B = (ll)(((__int128_t)A * x - 1) / y);
    
    if ((A % 2) == 0) {
        A += y;
        B += x;
    }
    
    ll Ax = mult(A, x), By = mult(B, y);

    add_op('^', Ax, By);   
    cout << ops.size() << "\n";
    for (auto s : ops) {
        cout << s << "\n";
    }
    
    return 0;
}