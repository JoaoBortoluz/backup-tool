#include "include/CLI11/CLI11.hpp"
#include <filesystem>
#include <iostream>
#include <string>

int main(int argc, char **argv) {
    CLI::App app{"Program to Backup your files"};

    int option = 0;
    std::string path = "~/code/Projects/";
    bool list;

    app.add_option("ls,--list", list, "List current files under backup whatching");
    app.add_option_group("add");

    CLI11_PARSE(app, argc, argv);

    if (list) {
        std::cout << "Listing current backups..." << std::endl;
        // listFunction();
    }

    return 0;
}
