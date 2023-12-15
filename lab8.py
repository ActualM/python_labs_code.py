from PIL import Image

def transparent(image_path):

    image = Image.open(image_path)


    img = image.convert("RGBA")


    data = img.getdata()


    new_data = []
    for i, (r, g, b, a) in enumerate(data):
        if i % 2 == 1:
            new_data.append((r, g, b, 0))
        else:
            new_data.append((r, g, b, a))


    img.putdata(new_data)


    output_path = image_path.replace('.', '_every_second_transparent.')
    img.save(output_path, "PNG")

    print(f"Изображение сохранено в {output_path}")


image_path = "C:\labpics\labimage.png"
transparent(image_path)
