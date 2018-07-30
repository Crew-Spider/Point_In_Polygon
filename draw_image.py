from PIL import Image, ImageDraw



black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)


def get_init_image(size=(500, 500)):
    image = Image.new('RGB', size, white)
    return image


def draw_polygon_to_image(verts, image, outline=black):
    draw = ImageDraw.Draw(image)

    # either use .polygon(), if you want to fill the area with a solid colour
    draw.polygon(verts, outline=outline)

    # or .line() if you want to control the line thickness, or use both methods together!
    # draw.line(tupVerts+[tupVerts[0]], width=2, fill=black)

    return image


def draw_points_to_image(points, image, fill=red):
    draw = ImageDraw.Draw(image)
    draw.point(points, fill=fill)
    return image


def draw_polygon(verts):
    image = get_init_image(size=(500, 500))
    image = draw_polygon_to_image(verts, image, outline=black)

    image.show()


def draw_polygon_and_inoutside_points(poly_verts, inside_points, outside_points, image_size=(500, 500)):
    image = get_init_image(size=image_size)
    image = draw_polygon_to_image(poly_verts, image)
    image = draw_points_to_image(inside_points, image, fill=red)
    image = draw_points_to_image(outside_points, image, fill=blue)

    image.show()


