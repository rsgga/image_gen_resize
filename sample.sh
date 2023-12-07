#!/bin/bash

set -eu

source openai_apikey.sh

curdir="$(cd $(dirname $0); pwd)"
image_dest_dirpath="${curdir}/images"

cd "${curdir}"

mkdir -p "${image_dest_dirpath}"

generated_file_name="generated_image.png"
resized_file_name="resized_image.png"
resoluted_file_name="resoluted_image.png"
re_resized_filed_name="re_resized_image.png"

generated_file_path="${image_dest_dirpath}/${generated_file_name}"
resized_file_path="${image_dest_dirpath}/${resized_file_name}"
resoluted_file_path="${image_dest_dirpath}/${resoluted_file_name}"
re_resized_filed_path="${image_dest_dirpath}/${re_resized_filed_name}"

image_width=256
image_height=256

resize_width=1024
resize_height=1024

# Generate PNG image.
echo 'Generating....'
#url=$(python3 ./image_generate.py "dall-e-3" "a girl, stencil art" "1024" "1024")
url=$(python3 ./image_generate.py "dall-e-2" "a girl, stencil art" "${image_width}" "${image_height}")

echo "Generated image URL: ${url}"

# Download generated image.
echo "Donwloading..."
wget -O "${generated_file_path}" "${url}"
echo "Downloaded file path: ${generated_file_path}"

# Adjust image resolution 
echo "Resoluting..."
python3 ./image_resolution.py "${generated_file_path}" "${resoluted_file_path}" "photo realistic, normal quality, masterpiece, an extremely delicate and beautiful, extremely detailed"
echo "Resoluted file path: ${resoluted_file_path}"

# Resize image
echo "Resizing...."
python3 ./image_resize.py "${resoluted_file_path}" "${resized_file_path}" "${resize_width}" "${resize_height}"
echo "Resized file path: ${resized_file_path}"

#echo "Resoluting..."
#python3 ./image_resolution.py "${resized_file_path}" "${resoluted_file_path}" "photo realistic, normal quality, masterpiece, an extremely delicate and beautiful, extremely detailed"
#echo "Resoluted file path: ${resoluted_file_path}"
#
#echo "Re resizing..."
#python3 ./image_resize.py "${resoluted_file_path}" "${re_resized_filed_path}" "${resize_width}" "${resize_height}"
#echo "Re resized file path: ${re_resized_filed_path}"

exit 0
