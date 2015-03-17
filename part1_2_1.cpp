#include "CPhys.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace CPhys;
using namespace std;
int blocks = 1e5;
int N = 1000;
long seed = 1;
double p = 0.1;

int main(){
    Vector xSampleVec = Vector(N);
    double* xSample = xSampleVec.getArrayPointer();
    Vector xVec = Vector(N);
    Vector xsqVec = Vector(N);
    xVec.reset();
    xsqVec.reset();
    double* x = xVec.getArrayPointer();
    double* xsq = xsqVec.getArrayPointer();
    int xi;
    for (int block = 0; block < blocks; block++) {
        xSample[0] = 1;
        xi = 1;
        for (int i = 1; i < N; i++) {
            double ran = Random::ran0(&seed);
            if (ran < p) xi = -xi;
            xSample[i] = xSample[i-1]+xi;
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
    cout << "Dumption positions to file : " << fName << endl;
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
