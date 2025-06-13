#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <ostream>
#include <string>

int create_dir_if_inexistent() {
    std::cout << "Filesystem" << std::endl;

    const char *home = std::getenv("HOME");

    std::cout << home << std::endl;

    std::filesystem::path origin_dir_path = "$HOME/code/Projects/backup-tool/";
    std::filesystem::path dest_dir_path = "$HOME/test/";

    std::filesystem::path test_path;

    std::cin >> test_path;

    std::cout << test_path << std::endl;

    if (!std::filesystem::exists(dest_dir_path)) {
        if (!std::filesystem::create_directories(dest_dir_path)) {
            std::cerr << "Failed to create dir: " << dest_dir_path << std::endl;
            return 1;
        }
        std::cout << "Created destination directorie " << dest_dir_path << std::endl;
    }

    std::filesystem::copy(origin_dir_path, dest_dir_path);
    
    return 0;
}
