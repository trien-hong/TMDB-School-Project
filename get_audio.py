# pylint: disable=C0114, C0116, R1710, R0911


def get_audio_file(movie_title: str):
    path = "/static/music/"

    audio_files = {
        "A Silent Voice: The Movie": [
            path + "To_Have_Been_In_Love.mp3",
            "Koi wo Shita no wa",
            "aiko",
        ],
        "Your Name.": [path + "It's_Nothing.mp3", "It's Nothing", "RADWIMPS"],
        "Weathering with You": [path + "Grand_Escape.mp3", "Grand Escape", "RADWIMPS"],
        "Words Bubble Up Like Soda Pop": [
            path + "Yamazakura.mp3",
            "Yamazakura",
            "Taeko Ohnuki",
        ],
        "The Garden of Words": [path + "Rain.mp3", "Rain", "Motohiro Hata"],
        "Steins;Gate: The Movie − Load Region of Déjà Vu": [
            path + "Like_Usual_At_That_Place.mp3",
            "Like Usual At That Place",
            "Ayane",
        ],
        "Liz and the Blue Bird": [path + "Songbirds.mp3", "Songbirds", "Homecomings"],
        "5 Centimeters per Second": [
            path + "One_More_Time_One_More_Chance.mp3",
            "One More Time, One More Chance",
            "Masayoshi Yamazaki",
        ],
        "Fate/stay night: Heaven's Feel III. Spring Song": [
            path + "Spring_Goes.mp3",
            "Spring Goes",
            "Aimer",
        ],
        "Evangelion: 2.0 You Can (Not) Advance": [
            path + "Beautiful_World.mp3",
            "Beautiful World",
            "Hikaru Utada",
        ],
        "Evangelion: 3.0+1.0 Thrice Upon a Time": [
            path + "One_Last_Kiss.mp3",
            "One Last Kiss",
            "Hikaru Utada",
        ],
        "Summer Wars": [
            path + "Our_Summer_Dreams.mp3",
            "Our Summer Dreams",
            "Tatsuro Yamashita",
        ],
    }

    audio_stats = audio_files.get(movie_title)

    return audio_stats[0], audio_stats[1], audio_stats[2]
