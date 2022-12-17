"""
This program generates a 6x6 pixel-art resembling those in
Github profile pictures.

*You can generate a random image by setting the word 
seed as 'random' while launching the program.

"""

import random
import argparse
from PIL import Image

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('word_seed', type=str, help='Word used for the image generation')
args = parser.parse_args()

def generate_pixel_art(word):
    # Join the ascii values of each character in the word
    seed = ''.join(str(ord(c)) for c in word)

    # Initialize the randomizer with the seed
    if(word=='random'):
        seed = random.random()
    random.seed(seed)

    # Initialize the grid with empty spaces
    grid = [[0 for _ in range(6)] for _ in range(6)]

    # Generate the pixels for the left half of the grid
    for i in range(6):
        for j in range(3):
            if random.random() > 0.5:

                grid[i][j] = 1

    # Invert and copy the left half into the right half
    for i in range(6):
        k=1
        for j in range(3,6):
            grid[i][j] = grid[i][j-k]
            k+=2
        
    return grid

# Call the function
grid = generate_pixel_art(args.word_seed)

# Generate the image
img = Image.new('RGB', (6,6))

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

for i in range(6):
    for j in range(6):
        if(grid[i][j]!=0):
            img.putpixel((i,j),color)
        else:
            img.putpixel((i,j),(255,255,255))

img = img.resize((1080,1080),resample=Image.BOX)
img = img.rotate(270)

# Show and save the image
img.show()
img.save(args.word_seed+'.png')

