import colorgram

colors = colorgram.extract('sample_of_color.jpg', 9)

colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_list.append(new_color)

print(colors_list)