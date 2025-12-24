#include <iostream>
#include <vector>
#include <random>
#include <fstream>
#include <chrono>
#define MATR_SIZE 10
double** newMatrix(int rows, int colums);
void delMatrix(int rows, int colums, double** matr);
void printMatrixTo(int rows, int colums, double** matr, std::ostream& stream);
void randomizeMatrix(int rows, int colums, double** matr);
bool multiplyMatrix(int rowsA, int columsA, double** matrA, int rowsB, int columsB, double** matrB, int rowsC, int columsC, double** matrC);
void readMatrixFrom(double** matr, int m, int n, std::istream& stream);

int main() {
	int m = MATR_SIZE;
	srand(time(NULL));
	double** A=newMatrix(m, m);
	double** B=newMatrix(m, m);
	double** C=newMatrix(m, m);
	/*
	std::ifstream fin("A.txt");
	readMatrixFrom(A, m, m, fin);
	fin.close();
	fin.open("B.txt");
	readMatrixFrom(B, m, m, fin);
	fin.close();
	*/
	randomizeMatrix(m, m, A);
	randomizeMatrix(m, m, B);
	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
	multiplyMatrix(m, m, A, m, m, B, m, m, C);
	std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
	printMatrixTo(m, m, C, std::cout);
	std::cout<<"Time: "<< std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count();
	delMatrix(m, m, A);
	delMatrix(m, m, B);
	delMatrix(m, m, C);
	return 0;
}

double** newMatrix(int rows, int colums) {
	double **matr = new double* [rows];
	for (int i = 0;i < rows;i++) {
		matr[i] = new double[colums];
	}
	return matr;
}

void printMatrixTo(int rows, int colums, double** matr, std::ostream& stream)
{
	for (int i = 0;i < rows;i++) {
		for (int j = 0;j < colums;j++)
			stream << matr[i][j] << " ";
		stream << std::endl;
	}
}

void readMatrixFrom(double **matr,int m, int n, std::istream& stream) {
	for (int i = 0;i < m;i++)
		for (int j = 0;j < n;j++)
			stream >> matr[i][j];
}


void randomizeMatrix(int rows, int colums, double** matr)
{
	for (int i = 0;i < rows;i++)
		for (int j = 0;j < colums;j++)
			matr[i][j] = (double)rand() / RAND_MAX;
}

void delMatrix(int rows,int colums,double** matr) {
	for (int i = 0;i < rows;i++)
		delete[] matr[i];
	delete[] matr;
}

bool multiplyMatrix(int rowsA, int columsA, double** matrA, int rowsB, int columsB, double** matrB, int rowsC, int columsC, double** matrC)
{
	if (columsA != rowsB)
		return false;
	if (rowsA != rowsC || columsB != columsC)
		return false;
	for (int i = 0;i < rowsC;i++) {
		for (int j = 0;j < columsC;j++)
			matrC[i][j] = 0;
		for (int j = 0;j < rowsB;j++) {
			for (int k = 0;k < columsC;k++) {
				matrC[i][k] += matrA[i][j] * matrB[j][k];
			}
		}
	}
	return true;
}