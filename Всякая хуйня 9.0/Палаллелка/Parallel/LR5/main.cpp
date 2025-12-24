#include <mpi.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include "matrixFuncs.h"
#include "communicateFuncs.h"
#include <chrono>
#define MATRIX_SIZE 10


int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
	MPI_Comm gridComm;
	int dims[2];
	int cords[2];
	createGridComm(MPI_COMM_WORLD,dims,cords,&gridComm);
	double** rowAbuff=nullptr;
	double** rowBbuff=nullptr;
	int rowLen = MATRIX_SIZE;
	int m = MATRIX_SIZE;
	int rowANum= dims[0]-1 != cords[0] ?(MATRIX_SIZE / dims[0]) : MATRIX_SIZE -(dims[0]-1)*(MATRIX_SIZE / dims[0]);
	int rowBNum= dims[1]-1 != cords[1] ?(MATRIX_SIZE / dims[1]) : MATRIX_SIZE -(dims[1]-1)*(MATRIX_SIZE / dims[1]);
	std::chrono::steady_clock::time_point begin,end;
	if (cords[0] == 0 && cords[1] == 0) {
		srand(time(NULL));
		double** matrA = randomizeMatrix(m, m);
		double** matrB = randomizeMatrix(m, m);
		/*
		std::ifstream fin("A.txt");
		double** matrA = readMatrixFrom(m, m,fin);
		fin.close();
		fin.open("B.txt");
		double** matrB = readMatrixFrom(m, m,fin);
		fin.close();
		*/
		begin = std::chrono::steady_clock::now();
		for(int i=0;i<dims[0];i++)
			for (int j = 0;j < dims[1];j++) {
				int rowsANumToSend= dims[0] - 1 !=i ? (MATRIX_SIZE / dims[0]) :  MATRIX_SIZE - (dims[0] - 1) * (MATRIX_SIZE / dims[0]);
				int rowsBNumToSend = dims[1] - 1 != j ? (MATRIX_SIZE / dims[1]) : MATRIX_SIZE - (dims[1] - 1) * (MATRIX_SIZE / dims[1]);
				double** rowABuffToSend = createRowBuff(matrA, i * rowANum, rowsANumToSend, m);
				double** rowBBuffToSend = createRowBuff(matrB, j * rowBNum, rowsBNumToSend, m);
				if (i == 0 && j == 0) {
					rowAbuff = rowABuffToSend;
					rowBbuff = rowBBuffToSend;
				}
				else {
					int destCords[2];
					destCords[0] = i;
					destCords[1] = j;
					sendRowsBuffToCords(rowABuffToSend, rowsANumToSend, rowLen, destCords, gridComm);
					sendRowsBuffToCords(rowBBuffToSend, rowsBNumToSend, rowLen, destCords, gridComm);
					delMatrix(rowABuffToSend, rowsANumToSend, rowLen);
					delMatrix(rowBBuffToSend, rowsBNumToSend, rowLen);
				}
			}
		delMatrix(matrA, m, m);
		delMatrix(matrB, m, m);
	}
	else {
		int srcCords[2];
		srcCords[0] = 0;
		srcCords[1] = 0;
		rowAbuff = receiveRowsBuffFromCords(rowANum, rowLen, srcCords, gridComm);
		rowBbuff = receiveRowsBuffFromCords(rowBNum, rowLen,srcCords, gridComm);
	}
	int rowCNum = rowANum;
	double** rowCbuff = multiplyRows(rowAbuff, rowBbuff, rowANum, rowBNum, rowLen, cords[1]* (m / dims[1]));
	delMatrix(rowAbuff, rowANum, rowLen);
	delMatrix(rowBbuff, rowBNum, rowLen);
	int destRank;
	int srcRank;
	MPI_Cart_shift(gridComm, 1, -1, &srcRank, &destRank);
	if (cords[1] == 0) {
		if (dims[1] != 1) {
			double** recvCbuff = receiveRowsBuffFromRank(rowCNum, rowLen, srcRank, gridComm);
			sumRows(rowCbuff, recvCbuff, rowCNum, rowLen);
			delMatrix(recvCbuff, rowCNum, rowLen);
		}
		int destRank;
		int srcRank;
		MPI_Cart_shift(gridComm, 0, -1, &srcRank, &destRank);
		if (cords[0] == dims[0] - 1) 
			sendRowsBuffToRank(rowCbuff, rowCNum, rowLen, destRank, gridComm);
		else{
			double** matrC = nullptr;
			int recvRowsCNum = m - (cords[0] + 1) * rowCNum;
			double** recvCbuff = receiveRowsBuffFromRank(recvRowsCNum, rowLen, srcRank, gridComm);
			matrC = uniteMatrix(rowCbuff, recvCbuff, rowCNum, recvRowsCNum, rowLen);
			delMatrix(recvCbuff, recvRowsCNum, rowLen);
			if (cords[0] == 0) {
				end= std::chrono::steady_clock::now();
				printMatrixTo(matrC,m, m, std::cout);
				std::cout << "Time: " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << std::endl;;
			}
			else {
				sendRowsBuffToRank(matrC, rowCNum+ recvRowsCNum,rowLen, destRank, gridComm);
			}
			delMatrix(matrC, rowCNum + recvRowsCNum, rowLen);
		}
	}
	else if (cords[1] == dims[1] - 1) {
		sendRowsBuffToRank(rowCbuff, rowCNum, rowLen, destRank, gridComm);
	}
	else {
		double** recvCbuff = receiveRowsBuffFromRank(rowCNum, rowLen, srcRank, gridComm);
		sumRows(rowCbuff, recvCbuff, rowCNum, rowLen);
		delMatrix(recvCbuff, rowCNum, rowLen);
		sendRowsBuffToRank(rowCbuff, rowCNum, rowLen, destRank, gridComm);
	}
	delMatrix(rowCbuff, rowCNum, rowLen);
	MPI_Comm_free(&gridComm);
    MPI_Finalize();
    return 0;
}


