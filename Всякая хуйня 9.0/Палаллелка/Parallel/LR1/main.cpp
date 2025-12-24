#include <mpi.h>
#include <iostream>
#include <random>
#include <iomanip>

#define MESSAGE_LENGTH 10

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int procNum, procRank;
    char message[MESSAGE_LENGTH];
    MPI_Status status;
    MPI_Comm_size(MPI_COMM_WORLD, &procNum);
    MPI_Comm_rank(MPI_COMM_WORLD, &procRank);
    if (procNum < 2) {
        std::cout << "Need 2 or more process" << std::endl;
        return -1;
    }
    srand((int)time(nullptr) + procRank);
    if (procRank == 0) {
        for (int i = 0;i < sizeof(message) - 1;i++)
            message[i] = (rand() % ('z' - 'a') + 'a');
        message[sizeof(message) - 1] = '\0';
        std::cout << "Starter send message: " << message << std::endl;
        double timer = MPI_Wtime();
        MPI_Send(message, strlen(message)+1, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
        MPI_Recv(message, sizeof(message), MPI_CHAR, procNum - 1, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        timer = MPI_Wtime() - timer;
        timer *= 1000;
        std::cout << "Ender recive message: " << message << std::endl;
        std::cout << std::fixed << std::setprecision(2) << "Work time: " << timer << std::endl;
    }else {
        MPI_Recv(message, sizeof(message), MPI_CHAR, procRank - 1, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        message[rand() % strlen(message)] = (rand() % ('z' - 'a') + 'a');
        MPI_Send(message, strlen(message)+1, MPI_CHAR, (procRank == (procNum - 1)) ? 0 : (procRank + 1), 0, MPI_COMM_WORLD);
    }
    MPI_Finalize();
    return 0;
}
