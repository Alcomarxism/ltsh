#pragma once
#include <iostream>

double** newMatrix(int m,int n);
double** createRowBuff(double **matr, int rowSt,int rowNum,int rowLen);
void delMatrix(double** matr, int m,int n);
void printMatrixTo(double** matr, int m,int n, std::ostream& stream);
double **readMatrixFrom(int m,int n, std::istream& stream);
double **randomizeMatrix(int m,int n);
void fillMatrix(double** matr, int m,int n, double num);
double** multiplyRows(double** rowBuffA, double** rowBuffB, int rowANum, int rowBNum, int rowLen, int colAStart);
void sumRows(double** rowBuffA, double **rowBuffB,int rowNum, int rowLen);
double** uniteMatrix(double** rowsA, double** rowsB, int rowANum, int rowBNum, int rowLen);