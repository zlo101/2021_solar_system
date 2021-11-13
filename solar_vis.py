# coding: utf-8
# license: GPLv3

"""
Visualization module.
Screen coordinates of the objects are used only here.
The functions for drawing and relocating the objects take in the model coordinates.
"""

header_font = "Arial-16"
"""Font in the heading"""

window_width = 800
window_height = 800
"""The window's width and height respectively"""

scale_factor = None
"""The ratio of the screen coordinates to the model ones. 
Type: float. Measure: the number of pixels in one meter."""


def calculate_scale_factor(max_distance):
    """Calculates the value of scale_factor based on the particular value of length taken in"""
    global scale_factor
    scale_factor = 0.4 * min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """
    Returns the x-coordinate (int) for the screen based on the x-coordinate of the model (float).
    Note: does not correct the result if, based on calculations, it is beyond the screen.

    :param x: the x-coordinate given by model calculation.
    """
    return int(x * scale_factor) + window_width // 2


def scale_y(y):
    """
    Returns the y-coordinate (int) for the screen based on the y-coordinate of the model (float).
    Note: does not correct the result if, based on calculations, it is beyond the screen.
    Note: the axis' direction is inverted so that the model's axis points up.

    :param y: the y-coordinate given by model calculation.
    """
    return (-1) * int(y * scale_factor) + window_height // 2


def create_star_image(space, star):
    """
    Draws the object of the 'Star' class on the canvas.

    :param space: canvas.
    :param star: object.
    """
    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """
    Draws the object of the 'Planet' class on the canvas.

    :param space: canvas.
    :param planet: object.
    """
    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_system_name(space, system_name):
    """
    Creates the text with the celestial objects on the canvas.
    Or, updates the text if the canvas already had it.

    :param space: canvas.
    :param system_name: name of the system.
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body):
    """
    Updates the object's position on the canvas

    :param space: canvas.
    :param body: body to be moved.
    """
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2 * r, window_height + 2 * r)  # beyond the screen
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
