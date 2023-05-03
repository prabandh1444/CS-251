
#include <iostream>
#include <string>
#include"hashing.hpp"
using namespace std;
int hash_string(string s,int N){
int hash=0;
    int x=67;
    long x_pow = 1;
    int i=0;
    while(int(s[i]!=0)) {
        hash = (hash + (int(s[i])) * x_pow);
        x_pow = (x_pow * x) ;
        i++;
    }
    return hash%N;
}
