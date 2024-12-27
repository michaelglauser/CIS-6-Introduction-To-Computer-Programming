
# 9.15 LAB: Artwork label (classes/constructors)

# Define the Artist class with a constructor to initialize an artist's information and a print_info() method. The constructor should by default initialize the artist's name to "unknown" and the years of birth and death to -1. print_info() displays "Artist:", then a space, then the artist's name, then another space, then the birth and death dates in one of three formats:
# 
#     (XXXX to YYYY) if both the birth and death years are nonnegative
#     (XXXX to present) if the birth year is nonnegative and the death year is negative
#     (unknown) otherwise

# Define the Artwork class with a constructor to initialize an artwork's information and a print_info() method. The constructor should by default initialize the title to "unknown", the year created to -1, and the artist to use the Artist default constructor parameter values.

# Ex: If the input is:

# Pablo Picasso
# 1881
# 1973
# Three Musicians
# 1921

# the output is:

# Artist: Pablo Picasso (1881 to 1973)
# Title: Three Musicians, 1921

# Ex: If the input is:

# Brice Marden
# 1938
# -1
# Distant Muses
# 2000

# the output is:

# Artist: Brice Marden (1938 to present)
# Title: Distant Muses, 2000

# Ex: If the input is:

# Banksy
# -1
# -1
# Balloon Girl
# 2002

# the output is:

# Artist: Banksy (unknown)
# Title: Balloon Girl, 2002

class Artist:  

    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year


    def print_info(self):
        year_info = "" 
        if self.birth_year >= 0 and self.death_year < 0:
            year_info = str(self.birth_year) + " to present"
        elif self.birth_year < 0:
            year_info = "unknown"
        else: 
            year_info = str(self.birth_year) + " to " + str(self.death_year)
        print(f"Artist: {self.name} ({year_info})") 


class Artwork:  


    def __init__(self, title="unknown", year_created=-1, artist="Artist"):
        self.title = title
        self.year_created = year_created
        self.artist = artist


    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":  
    user_artist_name = input()  
    user_birth_year = int(input())  
    user_death_year = int(input())  
    user_title = input()  
    user_year_created = int(input())  

  
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)


    user_artwork = Artwork(user_title, user_year_created, user_artist)


    user_artwork.print_info()


