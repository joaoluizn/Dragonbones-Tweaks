import argparse
import os
import sys
import json
import shutil

from PIL import Image
from glob import glob
from pathlib import Path

def rename_sequence_export(path):
    for json_file in glob(os.path.join(path, '*.json')):
        general_name = os.path.split(os.path.splitext(json_file)[0])[-1]
        with open(json_file, 'r') as inp_file:
            json_tex = json.load(inp_file)
            target = json_tex.get('SubTexture')[0].get('name')
            json_tex.update({'imagePath': f'{target}.png'})

        with open(json_file, 'w') as out_file:
            json.dump(json_tex, out_file)

        source_name = os.path.join(path, general_name)
        target_name = os.path.join(path, target)
        os.rename(f'{source_name}.png', f'{target_name}.png')
        os.rename(f'{source_name}.json', f'{target_name}.json')

def create_output_folder(path):
    output_path = os.path.join('output', Path(path).name)
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    shutil.copytree(path, output_path)
    return output_path

def create_gif(path, fps=30, format=".png"):
    gif_name = Path(path).name
    file_list = [Path(k) for k in glob(os.path.join(path, f'*{format}'))]
    sorted_file_list = sorted(file_list, key=lambda x: int(x.name.split('_')[1].split(format)[0]))
    pillow_img_list = [Image.open(img) for img in sorted_file_list]
    pillow_img_list[0].save(f'output/{gif_name}.gif',
               save_all=True,
               append_images=pillow_img_list[1:],
               duration=fps,
               loop=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--anim-folder-path",
    help="Folder path containing both assets and json from DragonBones Export")

    parser.add_argument("--gif", action='store_true',
    help="If enabled, a gif will be generated.")

    parser.add_argument("--gif-fps", default=30, type=int,
    help="Adjust gif fps output.")

    if not os.path.exists('output'):
        os.mkdir('output')

    args = parser.parse_args()
    required_folder = args.anim_folder_path
    if required_folder:
        export_folder = Path(args.anim_folder_path)
        if export_folder.is_dir() \
            and list(export_folder.glob('*.png')) \
                and list(export_folder.glob('*.json')):
            path = create_output_folder(export_folder)
            rename_sequence_export(path)
            if args.gif:
                create_gif(path, args.gif_fps)
        else:
            raise BaseException("Given folder doesn't exist or wrong folder")
    else:
        raise BaseException("Missing Export Folder")
