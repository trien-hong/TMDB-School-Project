# pylint: disable=C0114, C0116, R1710, R0911


def get_background_file(movie_title: str):
    path = "/static/background_images/"

    background_files = {
        "A Silent Voice: The Movie": path + "A_Silent_Voice.jpg",
        "Your Name.": path + "Your_Name.jpg",
        "Weathering with You": path + "Weathering_With_You.jpg",
        "Words Bubble Up Like Soda Pop": path + "Words_Bubble_Up_Like_Soda_Pop.jpg",
        "The Garden of Words": path + "Garden_Of_Words.jpg",
        "Steins;Gate: The Movie − Load Region of Déjà Vu": path + "Steins_Gate.jpg",
        "Liz and the Blue Bird": path + "Liz_And_The_Blue_Bird.jpg",
        "5 Centimeters per Second": path + "5_CM_Per_Second.jpg",
        "Evangelion: 2.0 You Can (Not) Advance": path + "Evangelion_2.0.jpg",
        "Fate/stay night: Heaven's Feel III. Spring Song": path + "Fate_Stay_Night.jpg",
        "Evangelion: 3.0+1.0 Thrice Upon a Time": path + "Evangelion_3.0+1.0.jpg",
        "Summer Wars": path + "Summer_Wars.jpg",
    }

    return background_files.get(movie_title)
