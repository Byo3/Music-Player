#pragma once
#include <vector>
#include <iostream>

class MusicPlayer{
    private:
        std::vector<std::string> song_infos;
        int index = 0;
        bool is_playing = true;

    public:
    void print_messages(std::string);
    void passing();
    void retrogressin();
    void shuffle();
    void pausing();
};
