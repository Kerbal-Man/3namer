#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(void) {
    cout << "Generating names!\n";
    fstream coolNames("coolNames.txt");
    string name = "";
    string charactors = "0123456789abcdefghijklmnopqrstuvwxyz_"; //37 total charactors // max index is 36
    int charactorLength = charactors.length();

    for (int i = 0; i < charactorLength; i++) {
        for (int j = 0; j < charactorLength; j++) {
            for (int k = 0; k < charactorLength; k++) {
                name = "";
                name += charactors[k];
                name += charactors[j];
                name += charactors[i];
                coolNames << name << "\n";

            }
        }
    }



    coolNames.close();

    return 0;
}