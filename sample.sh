#!/bin/bash

set -eu

OPENAI_API_KEY="xxxx"

curdir="$(cd $(dirname $0); pwd)"

cd "${curdir}"

generated_file_name='generated_image.png'
resized_file_name='resize_png_image.png'

echo 'Generating....'
#url=$(python3 ./image_generate.py "dall-e-3" "a girl, stencil art" "1024" "1024")
url=$(python3 ./image_generate.py "dall-e-2" "a girl, stencil art" "256" "256")

echo "Generated image URL: ${url}"

echo "Donwloading..."
wget -O "${generated_file_name}" "${url}"
echo "Downloaded file path: ${curdir}/${generated_file_name}"

echo "Resizing...."
python3 ./image_resize.py "./${generated_file_name}" "./${resized_file_name}" "1164" "498"
echo "Resized file path: ${curdir}/${resized_file_name}"

exit 0
