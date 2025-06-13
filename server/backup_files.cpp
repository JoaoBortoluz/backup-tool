#include <filesystem>
#include <iostream>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Uso: ./backup_exec <caminho_arquivo>" << std::endl;
        return 1;
    }

    std::filesystem::path origem = argv[1];
    std::filesystem::path destino = "/backups/" + origem.filename().string();

    try {
        std::filesystem::create_directories("/backups");
        std::filesystem::copy(origem, destino, std::filesystem::copy_options::overwrite_existing);
        std::cout << "Arquivo copiado para backup com sucesso." << std::endl;
    } catch (std::filesystem::filesystem_error& e) {
        std::cerr << "Erro ao copiar: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
