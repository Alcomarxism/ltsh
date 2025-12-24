#include <mpi.h>
#include <iostream>
#define GENFLOATNUM 1

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int procNum, procRank;
    MPI_Comm_rank(MPI_COMM_WORLD, &procRank);
    MPI_Comm_size(MPI_COMM_WORLD, &procNum);
    int dims=procNum;
    int periods = 1;
    MPI_Comm gridComm;
    MPI_Cart_create(MPI_COMM_WORLD, 1, &dims, &periods, 1, &gridComm);
    float f[GENFLOATNUM];
    float buff[GENFLOATNUM + MPI_BSEND_OVERHEAD];
    MPI_Buffer_attach(buff, (GENFLOATNUM+ MPI_BSEND_OVERHEAD) * sizeof(float));
    for(int i=0;i<GENFLOATNUM;i++)
        f[i] =(float)i+ procRank * 0.01f;
    MPI_Status status;
    MPI_Barrier(gridComm);
    double timer = MPI_Wtime();
    int srcRank, rcvRank;
    MPI_Cart_shift(gridComm, 0, -1, &srcRank, &rcvRank);
    MPI_Bsend(f, GENFLOATNUM, MPI_FLOAT, rcvRank,0, gridComm);
    MPI_Recv(f, GENFLOATNUM, MPI_FLOAT, srcRank,0, gridComm, &status);
    MPI_Barrier(gridComm);
    timer = MPI_Wtime() - timer;
    std::cout << "Proc " << procRank << " recive ";
    for (int i = 0;i < GENFLOATNUM;i++)
        std::cout << f[i] << " ";
    std::cout<<std::endl;
    MPI_Barrier(gridComm);
    if(procRank==0)
        std::cout << "Work time: " << timer * 1000 << std::endl;
    MPI_Comm_free(&gridComm);
    MPI_Finalize();
    return 0;
}
