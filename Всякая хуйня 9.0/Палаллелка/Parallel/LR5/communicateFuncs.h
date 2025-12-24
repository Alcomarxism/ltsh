#pragma once
#include <mpi.h>

void createGridComm(MPI_Comm oldComm, int dims[], int cords[], MPI_Comm* gridComm);
void sendRowsBuffToCords(double** rows, int rowsNum, int rowsLen, int* destCords, MPI_Comm gridComm);
double** receiveRowsBuffFromCords(int rowsNum, int rowsLen, int* srcCords, MPI_Comm gridComm);
double** receiveRowsBuffFromRank(int rowsNum, int rowsLen, int srcRank, MPI_Comm gridComm);
void sendRowsBuffToCords(double** rows, int rowsNum, int rowsLen, int* destCords, MPI_Comm gridComm);
void sendRowsBuffToRank(double** rows, int rowsNum, int rowsLen, int destRank, MPI_Comm gridComm);