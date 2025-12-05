#include <iostream>
#include <string>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>


int main(int argc, char *argv[]) {
    if (argc < 5) {
        std::cout << "Usage: ./client MACHINEID LEVEL MODULE MSG" << std::endl;
        return 1;
    }

    std::string machine = argv[1];
    std::string level = argv[2];
    std::string module = argv[3];
    std::string msg = argv[4];


    std::string payload = machine + "," + level + "," + module + "," + msg;


    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serv_addr;


    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5050);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);


    connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    send(sock, payload.c_str(), payload.size(), 0);
    close(sock);


    return 0;
}
