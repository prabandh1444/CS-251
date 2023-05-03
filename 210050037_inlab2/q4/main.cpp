#include <iostream>
#include <string>
#include "hashing.hpp"
using namespace std;
int main(int argc,char* argv[]) {
    cout << hash_string(argv[1],37) << endl;
}