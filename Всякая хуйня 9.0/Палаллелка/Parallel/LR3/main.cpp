#include <mpi.h>
#include <iostream>
#define GENINTNUM 3

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int procRank;
    MPI_Comm_rank(MPI_COMM_WORLD, &procRank);
    MPI_Comm newComm;
    MPI_Comm_split(MPI_COMM_WORLD, procRank % 3 == 0 ? 1 : MPI_UNDEFINED, procRank / 3, &newComm);
    if (procRank % 3 == 0) {
        int procNum;
        MPI_Comm_size(newComm, &procNum);
        MPI_Comm_rank(newComm, &procRank);
        int arr[GENINTNUM];
        int *rcvarr = new int[procNum * GENINTNUM];
        for (int i = 0;i < GENINTNUM;i++)
            arr[i] =(i+1)*100+procRank;
        MPI_Barrier(newComm);
        double timer = MPI_Wtime();
        MPI_Gather(arr, GENINTNUM, MPI_INT, rcvarr, GENINTNUM, MPI_INT, 0, newComm);
        timer = MPI_Wtime() - timer;
        if (procRank == 0) {
            for (int i = 0;i < procNum * GENINTNUM;i++) {
                if (i % GENINTNUM == 0)
                    std::cout << "From rank " << i*3 / GENINTNUM << ": ";
                std::cout << rcvarr[i] << " ";
                if ((i + 1) % GENINTNUM == 0)
                    std::cout << std::endl;
            }
            std::cout << "Work time: " << timer * 1000 << std::endl;
        }
        delete[] rcvarr;
        MPI_Comm_free(&newComm);
    }
    MPI_Finalize();
    return 0;
}
