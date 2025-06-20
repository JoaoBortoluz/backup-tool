#include <filesystem>
#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: ./backup_exec <file_path>" << std::endl;
        return 1;
    }

    std::filesystem::path source = argv[1];
    std::filesystem::path destination = std::filesystem::path(getenv("HOME")) / "backups" / source.filename();

    try {
        std::filesystem::create_directories(destination.parent_path());
        std::filesystem::copy(source, destination, std::filesystem::copy_options::overwrite_existing);
        std::cout << "File copied to backup: \"" << destination << "\"" << std::endl;
    } catch (std::filesystem::filesystem_error& e) {
        std::cerr << "Copy error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
