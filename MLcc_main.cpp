#include <iostream>
#include <iomanip>
#include <vector>
#include <string>

using namespace std;

int main(){

    string firstName, middleName, lastName;

    // create an array
    string arrayI[20];
    string arrayC[4];

    // creating pointer
    char n;
    char y = 'y';

    // Initializing arrayI values to 0
    for (int i = 0; i < 20; i++){
        arrayI[i] = "0";
    }
    // for (int i = 0; i < 20; i++){
    //     cout << arrayI[i] << endl;
    // }
    while (y == 'y'){
    // Asking for name, first, middle, and last in that order.
    cout << "First name: ";
    cin >> firstName;
    cout << "Middle name: ";
    cin >> middleName;
    cout << "Last name: ";
    cin >> lastName;
    n = firstName[0];  
    int i = 0;
    while(arrayI[i] != "0"){ i++; }
    arrayI[i] = n;

    cout << "Enter more name? ";
    cin >> y;
    }
    cout << endl;
    
    // Displaying the name that was entered.
    cout << firstName << " " << middleName << " " << lastName << endl;


    for (int i = 0; i < 20; i++){
        cout << arrayI[i] << endl;
    }
    
    return 0;
}