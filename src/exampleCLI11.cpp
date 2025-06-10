#include "../include/CLI11/CLI11.hpp"
#include <iostream>

int main(int argc, char** argv) {
    CLI::App app{"Backup Tool"};

    std::string target_dir;
    std::string mode = "full";
    bool list = false;

    app.add_option("--dir", target_dir, "Directory to back up");
    app.add_option("--mode", mode, "Backup mode (full/incremental)");
    app.add_flag("--list", list, "List previous backups");
    
    CLI11_PARSE(app, argc, argv);

    if (list) {
        std::cout << "Listing backups...\n";
        // your logic here
    } else if (!target_dir.empty()) {
        std::cout << "Backing up: " << target_dir << " using mode: " << mode << "\n";
        // your backup logic here
    } else {
        std::cout << app.help() << std::endl;
    }

    return 0;
}

// cp build/BackupGui /usr/local/bin/backup-tool
// chmod +x /usr/local/bin/backup-tool
