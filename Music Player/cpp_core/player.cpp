// * files from player
#include "player.h"

// ! Preprocess from c++
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

    using ERRORS = std::map<std::string, std::string>;
    inline ERRORS error_messanges = {
        {"impossible_range", "ou have reached of the begining of you playlist."},
        {"end_range", "There is no music. Add more?"}
    };

MusicPlayer::MusicPlayer(){}

void MusicPlayer::print_messages(std::string mensages){
    std::cout << mensages << "\n";
}

void MusicPlayer::passing(){
    if (index > song_infos.size() - 1){
        print_messages(error_messanges["end_range"]);

    } else {
    index += 1;
    print_messages(song_infos[index]);
    }
}

void MusicPlayer::retrogressin(){
    if (index <= 0){
        print_messages(error_messanges["impossible_range"]);
    } else {
    index -= 1;
    print_messages(song_infos[index]);
    }
}

void MusicPlayer::shuffle(){}

void MusicPlayer::pausing(){
    is_playing = !is_playing;
    if (! is_playing){
        print_messages("Pausado");
    } else {
    print_messages("Despausado");
    }
}
