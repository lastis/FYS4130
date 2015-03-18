#include "CPhys.h"
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>     // Adds atof function.

using namespace CPhys;
using namespace std;
int blocks = 1e5;
int N = 10000;
int nBins = 201;
double nMax = 301;
double nMin = -301;
long seed = 1;
double p = 0.5;

int main(int argc, const char *argv[]){
    // Second argument is the file name, third is the p-value.
    if (argc == 3) p = atof(argv[2]);
    cout << "P = " << p << endl;

    double x = 0;
    Vector binsVec = Vector(nBins);
    binsVec.reset();
    double* bins = binsVec.getArrayPointer();
    for (int i = 0; i < nBins; i++) {
        if (bins[i] != 0) cout << bins[i] << "nooo "<< endl;
    }
    int xi, bin;
    for (int block = 0; block < blocks; block++) {
        x = 1;
        xi = 1;
        for (int i = 1; i < N; i++) {
            double ran = Random::ran0(&seed);
            if (ran < p) xi = -xi;
            x = x+xi;
            if (x >= nMax || x < nMin) continue;
            bin = (x - nMin)/(nMax - nMin)*nBins;
            bins[bin] += 1;
        }
    }
    for (int i = 0; i < nBins; i++) {
        bins[i] /= blocks*N;
    }

    Vector nVec = Vector(nBins);
    nVec.linspace(nMin,nMax);
    double* n = nVec.getArrayPointer();

    string fName;
    if (argc == 3) fName = argv[1];
    else fName = "x1_5_1.dat";
    string adress = fName;
    ofstream myFile;
    cout << "Dumption positions to file : " << fName << endl;
    myFile.open(adress.c_str());
    for (int i = 0; i < nBins; i++) {
        myFile << bins[i] << " ";
    }
    myFile << endl;
    for (int i = 0; i < nBins; i++) {
        myFile << n[i] << " ";
    }
    myFile << endl;
    myFile.close();
    return 0;
}
