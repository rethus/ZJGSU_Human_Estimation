import os
import os.path as osp
import sys

sys.path.insert(0, osp.abspath('../'))

from tqdm import tqdm
import logging

from utils.utils_folder import list_immediate_childfile_paths, create_folder
from utils.utils_video import video2images, image2video

zero_fill = 8

logger = logging.getLogger(__name__)


def Video(base_video_path):
    logger.info("Start")

    video_list = list_immediate_childfile_paths(base_video_path, ext=['mp3', 'mp4'])

    input_image_save_dirs = []

    for video_path in tqdm(video_list):
        video_name = osp.basename(video_path)
        temp = video_name.split(".")[0]
        image_save_path = os.path.join(base_video_path, temp)
        input_image_save_dirs.append(image_save_path)

        create_folder(image_save_path)

        video2images(video_path, image_save_path)  # jpg
