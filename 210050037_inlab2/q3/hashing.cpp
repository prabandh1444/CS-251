
#include <iostream>
#include <string>
#include"hashing.hpp"
using namespace std;
int value;
int hash_string(string s,int k){
k=37;
int i=0;
while(int(s[i])!=0){
value=value+int(s[i]);
i++;
}
value=value%k;
return value;
}