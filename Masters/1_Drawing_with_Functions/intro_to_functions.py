import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def draw_cloud():
    """ Draw a cloud """

    #cloud
    arcade.draw_ellipse_filled(650, 500, 80, 80, arcade.color.WHITE, 0)
    arcade.draw_ellipse_filled(570, 480, 55, 50, arcade.color.WHITE, 0)
    arcade.draw_ellipse_filled(730, 460, 50, 50, arcade.color.WHITE, 0)

def draw_rollinghills():
    """ Draw rolling hills """

    #rolling hills
    arcade.draw_ellipse_filled(600, -10, 300, 100, arcade.color.ISLAMIC_GREEN, 20)
    arcade.draw_ellipse_filled(100, -200, 500, 400, arcade.color.KELLY_GREEN, 0)

def draw_trees():
    """ Draw trees """

    #trees
    arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.WOOD_BROWN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rollinghills()
    draw_trees()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()