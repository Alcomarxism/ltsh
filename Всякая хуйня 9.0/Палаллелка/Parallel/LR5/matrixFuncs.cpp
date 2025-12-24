#include "matrixFuncs.h"

double** newMatrix(int m, int n) {
	double** matr = new double* [m];
	for (int i = 0;i < m;i++) {
		matr[i] = new double[n];
	}
	return matr;
}
double** createRowBuff(double** matr, int rowSt, int rowNum,int rowLen) {
	double** rowBuff = new double* [rowNum];
	for (int i = 0;i < rowNum;i++) {
		rowBuff[i] = new double[rowLen];
		for (int j = 0;j < rowLen;j++)
			rowBuff[i][j] = matr[i + rowSt][j];
	}
	return rowBuff;
}
void delMatrix(double** matr, int m, int n) {
	for (int i = 0;i < m;i++)
		delete[] matr[i];
	delete[] matr;
}
void printMatrixTo(double** matr, int m, int n, std::ostream& stream) {
	for (int i = 0;i < m;i++) {
		for (int j = 0;j < n;j++)
			stream << matr[i][j] << " ";
		stream << std::endl;
	}
}

double **readMatrixFrom(int m, int n, std::istream& stream){
	double** matr = newMatrix(m, n);
	for (int i = 0;i < m;i++) 
		for (int j = 0;j < n;j++)
			stream >> matr[i][j];
	return matr;
}

double **randomizeMatrix( int m,int n){
	double** matr = newMatrix(m, n);
	for (int i = 0;i < m;i++)
		for (int j = 0;j < n;j++)
			matr[i][j] = (double)rand() / RAND_MAX;
	return matr;
}

void fillMatrix(double** matr, int m,int n, double num){
	for (int i = 0;i < m;i++)
		for (int j = 0;j < n;j++)
			matr[i][j] = num;
}

double** multiplyRows(double** rowBuffA, double** rowBuffB, int rowANum,int rowBNum, int rowLen,int colAStart){
	double** res = new double* [rowANum];
	for (int i = 0;i < rowANum;i++) {
		res[i] = new double[rowLen];
		for (int j = 0;j < rowLen;j++)
				res[i][j] = 0;
		for (int j = 0;j < rowBNum;j++) {
			for (int k = 0;k < rowLen;k++) {
				res[i][k] += rowBuffA[i][colAStart+j] * rowBuffB[j][k];
			}
		}
	}
	return res;
}

void sumRows(double** rowBuffA, double** rowBuffB, int rowNum, int rowLen) {
	for (int i = 0;i < rowNum;i++)
		for (int j = 0;j < rowLen;j++)
			rowBuffA[i][j] += rowBuffB[i][j];

}
double** uniteMatrix(double** rowsA, double** rowsB, int rowANum, int rowBNum, int rowLen) {
	double** res = newMatrix(rowANum + rowBNum, rowLen);
	for (int i = 0;i < rowANum;i++)
		for (int j = 0;j < rowLen;j++)
			res[i][j] = rowsA[i][j];
	for (int i = 0;i < rowBNum;i++)
		for (int j = 0;j < rowLen;j++)
			res[i+rowANum][j] = rowsB[i][j];
	return res;
}