import fresh_tomatoes
"""It imports the fresh_tomatoes module"""
import media
"""It imports the media module"""

#Create instances as below. star_wars is an instance
star_wars = media.Movie("PG-13", "Star Wars: The Last Jedi", "The further adventures of Luke Skywalker (Mark Hamill), Leia (Carrie Fisher) and Rey (Daisy Ridley)", "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg", "https://www.youtube.com/watch?v=zB4I68XVPzQ", "Rian Johnson", "English", "USA")

boss_baby = media.Movie("G", "The Boss Baby", "A new baby's arrival impacts a family, told from the point of view of a delightfully unreliable narrator", "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg","https://www.youtube.com/watch?v=tquIfapGVqs", "Marla Frazee", "English", "USA")

cars3 = media.Movie("G", "Cars 3", "Blindsided by a new generation of blazing-fast cars, the legendary Lighting McQueen finds", "https://upload.wikimedia.org/wikipedia/en/9/94/Cars_3_poster.jpg", "https://www.youtube.com/watch?v=2LeOH9AGJQM", "Brian Fee", "English", "USA")

guardians = media.Movie("PG-13", "The Guardians Of The Galaxy 2", "Peter Quill and his fellow Guardians are hired by a powerful alien race to protect their precious batteries from invaders", "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg", "https://www.youtube.com/watch?v=2cv2ueYnKjg", "James Gunn", "English", "USA")

lego_ninjago = media.Movie("G", "The Lego Ninjago movie", "Six young ninjas Lloyd, Jay, Kai, Cole, Zane and Nya are tasked with defending their island home, called Ninjago.", "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Lego_Ninjago_Movie.jpg", "https://www.youtube.com/watch?v=sbMfKs0PwcM", "Hilary Winston", "English", "USA")

transformer = media.Movie("PG-13", "Transformers: The Last Knight", "Humans are at war with the Transformers, and Optimus Prime is gone. The key to saving the future.", "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg", "https://www.youtube.com/watch?v=yCOvcyfRPRk", "Akiva Goldsman", "English", "USA")

naagin = media.Tvshow("PG", "Naagin season1", "Shape-shifting serpents want to avenge parents' death", "https://upload.wikimedia.org/wikipedia/commons/3/3b/Naagin_2_title.jpg", "https://www.youtube.com/watch?v=RAq0uIpXRV4", "Mrinal Jha", "Hindi", "India")

raymond = media.Tvshow("PG-13", "Everybody Loves Raymond", "About Family &Comedy", "http://images.uncyclomedia.co/uncyclopedia/en/9/9e/WikiRay.jpg", "https://www.youtube.com/watch?v=enTKltmtlnE", "Philip Rosenthal", "English", "USA")

chinnari = media.Tvshow("PG-13", "Chinnari Pelli Kuthuru", " About Child Marriage", "https://upload.wikimedia.org/wikipedia/commons/b/b8/Balikavadhubalikavadhu.jpg", "https://www.youtube.com/watch?v=aCDCizmZN4c", "Purnendu Shekhar", "Telugu", "India")


#Keep all the moviesin a list and tv shows in a different list
#Now I have this lists of movies, tv shows . I can give these lists as input to the open_movies_page function
#So I will provide movies, tvshows as arguments to the open _movies_page function
movies = [star_wars, boss_baby, cars3, guardians, lego_ninjago, transformer]
tvshows = [naagin, raymond, chinnari]
#Call the function open movies page
fresh_tomatoes.open_movies_page(movies, tvshows)

 

