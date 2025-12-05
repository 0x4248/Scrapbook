#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>


void log_to_csv(const std::string &machine, const std::string &line) {
    std::string filename = machine + ".csv";
    std::ofstream file(filename, std::ios::app);
    if (!file.is_open()) {
        std::cerr << "[PulseMSG] ERROR: Cant write to " << filename << std::endl;
        return;
    }
    file << line << "\n";
}

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);


    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt));


    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(5050);

    int x;
    x = bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 3);
    while (true) {
        new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
        char buffer[2048] = {0};
        int valread = read(new_socket, buffer, 2048);


        std::string data(buffer);
        std::stringstream ss(data);
        std::string machine, level, module, msg;


        std::getline(ss, machine, ',');
        std::getline(ss, level, ',');
        std::getline(ss, module, ',');
        std::getline(ss, msg);


        std::string csv_line = level + "," + module + "," + msg;
        log_to_csv(machine, csv_line);
        close(new_socket);
    }
}
