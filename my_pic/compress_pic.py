# from PIL import Image

# def compress_image(input_image_path, output_image_path, quality=30):
#     with Image.open(input_image_path) as image:
#         image.save(output_image_path, 'PNG', optimize=True, quality=quality)

# input_image_path = 'prof_pic.png'
# output_image_path = 'prof_pic_output.png'

# compress_image(input_image_path, output_image_path, quality=30)



# from PIL import Image

# def compress_image(input_image_path, output_image_path, quality=30):
#     with Image.open(input_image_path) as image:
#         image.save(output_image_path, 'PNG', optimize=True, quality=quality)

# if __name__ == '__main__':
#     input_image_path = 'prof_pic.png'
#     output_image_path = 'prof_pic_output.png'
#     quality = 30

#     compress_image(input_image_path, output_image_path, quality)



from PIL import Image

def compress_image(input_image_path, output_image_path, quality=30):
    with Image.open(input_image_path) as image:
        image.save(output_image_path, 'JPEG', optimize=True, quality=quality)

if __name__ == '__main__':
    input_image_path = 'prof_pic.png'
    output_image_path = 'prof_pic_output.jpg'
    quality = 30

    compress_image(input_image_path, output_image_path, quality)
