import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def draw_cloud(x, y, z):
    """ Draw a cloud """

    #cloud
    arcade.draw_ellipse_filled(x, y, z, z, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x-80, y-20, z-25, z-25, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x+80, y-40, z-30, z-30, arcade.color.WHITE)


def draw_rollinghills():
    """ Draw rolling hills """

    #rolling hills
    arcade.draw_ellipse_filled(600, -10, 300, 100, arcade.color.ISLAMIC_GREEN, 20)
    arcade.draw_ellipse_filled(100, -200, 500, 400, arcade.color.KELLY_GREEN, 0)

def draw_trees():
    """ Draw trees """

    #base
    arcade.draw_rectangle_filled(160, 100, 50, 100, arcade.color.BROWN_NOSE)

    #leaves
    arcade.draw_triangle_filled(200, 100, 300, 100, 200, 50, arcade.color.UP_FOREST_GREEN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)
    arcade.start_render()

   # call your draw functions
    #arcade.draw_ellipse_filled(650, 500, 80, 80, arcade.color.WHITE, 0)
    #arcade.draw_ellipse_filled(570, 480, 55, 50, arcade.color.WHITE, 0)
    #arcade.draw_ellipse_filled(730, 460, 50, 50, arcade.color.WHITE, 0)
    draw_cloud(650, 500, 80)
    draw_cloud(150, 500, 80)

    draw_rollinghills()
    draw_trees()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()