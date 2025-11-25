cmake_minimum_required(VERSION 3.10)
project(Pulse)

set(CMAKE_CXX_STANDARD 17)

add_executable(server src/server.cpp)
add_executable(pulsemsg_client src/client.cpp)

# Link pthread for server if needed in future
target_link_libraries(pulsemsg_server pthread)
