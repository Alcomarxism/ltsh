#include "communicateFuncs.h"
#include "matrixFuncs.h"
#include <cmath>
double **receiveRowsBuffFromCords(int rowsNum, int rowsLen, int* srcCords, MPI_Comm gridComm) {
	int srcRank;
	MPI_Cart_rank(gridComm, srcCords, &srcRank);
	return receiveRowsBuffFromRank(rowsNum, rowsLen, srcRank, gridComm);
}
double** receiveRowsBuffFromRank(int rowsNum, int rowsLen, int srcRank, MPI_Comm gridComm) {
	double** recvBuff = newMatrix(rowsNum, rowsLen);
	MPI_Status status;
	for (int i = 0;i < rowsNum;i++) {
		MPI_Recv(recvBuff[i], rowsLen, MPI_DOUBLE, srcRank, 0, gridComm, &status);
	}
	return recvBuff;
}
void sendRowsBuffToCords(double** rows, int rowsNum, int rowsLen, int* destCords, MPI_Comm gridComm) {
	int destRank;
	MPI_Cart_rank(gridComm,destCords,&destRank);
	sendRowsBuffToRank(rows, rowsNum, rowsLen, destRank, gridComm);
}
void sendRowsBuffToRank(double** rows, int rowsNum, int rowsLen, int destRank, MPI_Comm gridComm) {
	for (int i = 0;i < rowsNum;i++) {
		MPI_Send(rows[i], rowsLen, MPI_DOUBLE, destRank, 0, gridComm);
	}
}
void createGridComm(MPI_Comm oldComm, int dims[], int cords[], MPI_Comm* gridComm) {
	int procNum, procRank;
	MPI_Comm_size(MPI_COMM_WORLD, &procNum);
	MPI_Comm_rank(MPI_COMM_WORLD, &procRank);
	int pw = 0;
	while (!(procNum & 1)) {
		pw++;
		procNum >>= 1;
	}
	if (pw % 2 == 0) {
		dims[0] = dims[1] = (int)pow(2, pw / 2);
	}
	else {
		dims[1] = (int)pow(2, (pw - 1) / 2);
		dims[0] = (int)pow(2, (pw - 1) / 2 + 1);
	}
	int periods[2] = { 1,1 };
	MPI_Cart_create(MPI_COMM_WORLD, 2, dims, periods, 1, gridComm);
	MPI_Cart_coords(*gridComm, procRank, 2, cords);
}
