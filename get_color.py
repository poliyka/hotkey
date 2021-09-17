from PIL import ImageGrab


def get_color_hex(x, y):
    rgb = ImageGrab.grab().load()[x, y]
    return "#%02x%02x%02x" % rgb


def get_color_rgb(x, y):
    rgb = ImageGrab.grab().load()[x, y]
    return rgb


if __name__ == "__main__":
    print(get_color_hex(333, 333))
    print(get_color_rgb(333, 333))
