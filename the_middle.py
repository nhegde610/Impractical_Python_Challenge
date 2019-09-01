"""Generate funny names by random selection with the middle name."""
import sys
import random

def main():
    """Choose names at random from 3 tuples of name and print to screen."""
    print("Welcome to the Funny name.\n")
    print("A full awesome name for you:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    middle = ('Spanky', 'Animal', 'Hambone', 'Lumpy', 'Spum', 'T-Money',
              'Buzzy', 'Wheezy', 'Quarter', "Jimmy 'Seepage'", "White 'Stuff'",
              'Toastmaster', 'Butters', 'Breezy', 'Nitro', 'MilkMan', 'Lefty',
              'Saudi', 'Jewman', 'AssMan', 'Kokomo', 'Girth', 'Coop', 'Noah',
              'ShoeShine', 'Jigroid', 'Jigga', 'Porker', 'fat', 'balloon')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
            'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        first_name = random.choice(first)
        middle_name = random.choice(middle)
        last_name = random.choice(last)

        print("\n\n")
        print("{} {} {}".format(first_name, middle_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")

        if try_again.lower() == "n":
            break
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
