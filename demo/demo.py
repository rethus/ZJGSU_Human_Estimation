from run import Run
from video import Video
import os
import os.path as osp
import sys

sys.path.insert(0, osp.abspath('../'))

from tqdm import tqdm

from utils.utils_folder import list_immediate_childfile_paths, create_folder
from utils.utils_video import video2images, image2video

input_image_save_dirs = 'in/soccer'

if __name__ == '__main__':
    # Video('in')
    image_list = list_immediate_childfile_paths(input_image_save_dirs, ext='jpg')
    for index, image in tqdm(enumerate(image_list)):
        if index - 3 < 0 or index + 3 >= len(image_list): continue
        I0 = image_list[index - 3]
        I2 = image_list[index - 1]
        I4 = image_list[index + 1]
        I6 = image_list[index + 3]

        Run(I0, I2, 'out/temp/I1.jpg')
        Run(I2, I4, 'out/temp/I3.jpg')
        Run(I4, I6, 'out/temp/I5.jpg')

        I1 = 'out/temp/I1.jpg'
        I3 = 'out/temp/I3.jpg'
        I5 = 'out/temp/I5.jpg'

        Run(I1, I3, 'out/temp/I2.jpg')
        Run(I3, I5, 'out/temp/I4.jpg')

        I2 = 'out/temp/I2.jpg'
        I4 = 'out/temp/I4.jpg'

        Run(I2, I4, 'out/' + image.split('/')[-1])

        # print(index, image)
    # image2video(os.path.join('out', 'result'), 'result')
    print("------->Complete!")