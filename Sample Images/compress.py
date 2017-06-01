''' Module DocString Fill this'''
#run this in any directory with the max width parameter add -v for verbose

#image will be scalled in proportion to confine within the max width parameter
#this allows you to get images that are within a box
#dimension for online publishing without distorting the image

#get Pillow (fork of PIL) from pip before running --> pip install Pillow

#regarding timing: 42 seconds for 4938 so max 15 minutes for 100,000 images

import os
import argparse
from PIL import Image

def compress_me(file, max_dimension, verbose):
    '''Given filename compresses files and scales it to the given max
        dimensions without any returns for performance calculations'''

    filepath = os.path.join(os.getcwd(), file)

    oldsize = os.stat(filepath).st_size

    picture = Image.open(filepath)

    dim = picture.size

    ratio = (max_dimension/dim[0], max_dimension/dim[1])

    picture.thumbnail((dim[0]*ratio, dim[1]*ratio), Image.ANTIALIAS)
    picture.save('Compressed_'+file, 'JPEG', optimize=True, quality=85)

    newsize = os.stat(os.path.join(os.getcwd(), 'Compressed_'+file)).st_size
    percent = (oldsize-newsize)/float(oldsize)*100

    if verbose:
        print('File compressed from {} to {} or {}%'.format(oldsize, newsize, percent))



def compress_me_return(file, max_dimension, verbose, qual):
    '''Compresses all images in a given directory as JPEG, '''
    filepath = os.path.join(os.getcwd(), file)

    oldsize = os.stat(filepath).st_size

    picture = Image.open(filepath)

    dim = picture.size

    ratio = (max_dimension/dim[0], max_dimension/dim[1])

    picture.thumbnail((dim[0]*ratio, dim[1]*ratio), Image.ANTIALIAS)

    picture.save('Compressed_'+file, 'JPEG', optimize=True, quality=qual)

    newsize = os.stat(os.path.join(os.getcwd(), 'Compressed_'+file)).st_size
    percent = (oldsize-newsize)/float(oldsize)*100
    if verbose:
        print('File compressed from {} to {} or {}%'.format(oldsize, newsize, percent))
    return percent

def main():
    '''Main Function Pulls Command Line Args, Compresses Files in Current Dir'''
    parser = argparse.ArgumentParser(description='pyCompress')
    parser.add_argument('-v', "--verbose",
                        help='verbose flag to see each individual conversion',
                        action='store_true')

    parser.add_argument('-q', '--quality',
                        help='set int quality up to 100, default 85%',
                        type=int,
                        default=85)

    parser.add_argument('-d', '--dimension',
                        help='Set max dimension, images will scale within max edge',
                        type=int,
                        default=400)
    args = parser.parse_args()
    print(args)
    pwd = os.getcwd()
    tot = 0
    num = 0
    for file in os.listdir(pwd):
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            num += 1
            tot += compress_me_return(file, int(args.dimension),
                                      args.verbose, args.quality)
    print('Average Compression: {}'.format(float(tot)/num))
    print('Done')



if __name__ == '__main__':
    main()
