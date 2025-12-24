#include <mpi.h>
#include <iostream>
#define GENINTNUM 5

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int procNum, procRank;
    MPI_Comm_size(MPI_COMM_WORLD, &procNum);
    MPI_Comm_rank(MPI_COMM_WORLD, &procRank);
    int arr[GENINTNUM];
    int *rcvarr = new int[procNum * GENINTNUM];
    for (int i = 0;i < GENINTNUM;i++)
        arr[i] = procRank*GENINTNUM+i;
    MPI_Barrier(MPI_COMM_WORLD);
    double timer = MPI_Wtime();
    MPI_Gather(arr, GENINTNUM, MPI_INT, rcvarr, GENINTNUM , MPI_INT, 0, MPI_COMM_WORLD);
    timer = MPI_Wtime() - timer;
    if (procRank == 0) {
        for (int i = 0;i < procNum * GENINTNUM;i++) {
            if (i % GENINTNUM == 0)
                std::cout << "From rank "<<i/GENINTNUM<<": ";
            std::cout << rcvarr[i] << " ";
            if ((i+1)% GENINTNUM ==0)
                std::cout << std::endl;
        }
        std::cout << "Work time: " << timer * 1000 << std::endl;
    }
    delete[] rcvarr;
    MPI_Finalize();
    return 0;
}
