#include "CPhys.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace CPhys;
using namespace std;
int blocks = 1e5;
int N = 1000;
long seed = 2;
/* double p = 0.5; */
/* double p = 0.99; */
double p = 0.9;

int main(){
    Vector xSampleVec = Vector(N);
    /* Vector xsqSampleVec = Vector(N); */
    double* xSample = xSampleVec.getArrayPointer();
    /* double* xsqSample = xsqVec.getArrayPointer(); */
    Vector xVec = Vector(N);
    Vector xsqVec = Vector(N);
    double* x = xVec.getArrayPointer();
    double* xsq = xsqVec.getArrayPointer();
    for (int block = 0; block < blocks; block++) {
        for (int i = 1; i < N; i++) {
            double ran = Random::ran0(&seed);
            if (ran > p) xSample[i] = xSample[i-1]-1;
            else xSample[i] = xSample[i-1]+1;
        }
        for (int i = 0; i < N; i++) {
            x[i] += xSample[i];
            xsq[i] += xSample[i]*xSample[i];
        }
    }

    for (int i = 0; i < N; i++) {
        xsq[i] = xsq[i]/blocks;
        x[i] = x[i]/blocks;
    }



    string fName = "x.dat";
    string adress = fName;
    ofstream myFile;
    cout << "Dumption energies to file : " << fName << endl;
    myFile.open(adress.c_str());
    for (int i = 0; i < N; i++) {
        myFile << x[i] << " ";
    }
    myFile << endl;
    for (int i = 0; i < N; i++) {
        myFile << xsq[i] << " ";
    }
    myFile << endl;
    myFile.close();
    return 0;
}
