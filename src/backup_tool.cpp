#include "../include/CLI11/CLI11.hpp"
#include <filesystem>
#include <iostream>
#include <string>

int main(int argc, char **argv) {
    CLI::App app{"Program to Backup your files"};

    int option = 0;
    std::string path = "~/code/Projects/";

    app.add_option("ls,--list", path, "List current files under backup whatching");

    CLI11_PARSE(app, argc, argv);

    std::cout << "File path: " << path << std::endl;
    // std::cout << "===Backup app===\n";
    // std::cout << "Choose a option:\n1-Define filepath\n2-Restore backup\n";

    // std::cin >> option;
    // switch (option) {
    //     case 1:
    //
    // }
    // std::getline(std::cin, path);
    
    return 0;
}
