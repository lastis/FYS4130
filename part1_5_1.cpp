#include "CPhys.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace CPhys;
using namespace std;
int blocks = 1e5;
int N = 1000;
int nBins = 201;
double nMax = 100;
double nMin = -100;
long seed = 1;
double p = 0.5;

int main(){
    /* Vector xSampleVec = Vector(N); */
    /* double* xSample = xSampleVec.getArrayPointer(); */
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
        /* cout << bins[i] << endl; */
    }

    Vector nVec = Vector(nBins);
    nVec.linspace(nMin,nMax);
    double* n = nVec.getArrayPointer();

    string fName = "x.dat";
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
