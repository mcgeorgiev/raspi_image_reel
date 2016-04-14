try:
    import pygame
    import os
    import time
    import RPi.GPIO as GPIO
except ImportError as e:
    print 'Module could not be loaded: '
    print e


def get_paths():
    # load all the image paths in img_folder
    for dirpath, dirnames, filenames in os.walk('img_folder'):
        file_path_list = []
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_path_list.append(file_path)
    return file_path_list


def pygame_load(files):
    # loads images from file_path_list
    images = []
    for file in files:
        images.append(pygame.image.load(file))
    return images

    # *Following doesn't really do anything at the moment*
    '''
    for img in images:
        pygame.transform.scale(img, (1280,720))
        '''

def blit_images(images):
    for img in images:
        img = pygame.Surface(screen.get_size())
        img = img.convert()
        img.blit(img, (0,0))

# set up pygame
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


# set up GPIO
GPIO.setmode(GPIO.BOARD)
BUTTON = 11
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
                          # uses a pull down internal resistor

BACKGROUND_COLOUR = (0,0,0)

# load images
img_list = pygame_load(get_paths())
blit_imgs(img_list)

# blit the first image to the screen
current_img = 0
screen.blit(img_list[current_img], (0,0))
pygame.display.flip()

prev_input = 0
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    input = GPIO.input(BUTTON)

    if ((not prev_input) and input):
        screen.blit(img_list[current_img], (0,0))
        pygame.display.flip()
        current_img += 1
        if current_img == len(img_list):
            current_img = 0

    prev_input = input
    time.sleep(0.05)
    screen.fill(BACKGROUND_COLOUR)

pygame.quit()
