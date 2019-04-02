
import arcade
import

# set the text for the meme
line1 = "1goodVariableName"
line2 = "good_variable_name1"

# set the dimensions of the window, based on the image
height = 640
width = 550
arcade.open_window(height, width, "Meme Generator")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# load the image
texture = arcade.load_texture("images/drake_meme.jpg")
arcade.draw_texture_rectangle(texture.width//2, texture.height//2, texture.width,
                              texture.height, texture, 0)

# render the text
arcade.draw_text(line1, width//2 + 100, height - height//3, arcade.color.BLACK, 12)
arcade.draw_text(line2, width//2 + 100, height//2 - height//4,
                 arcade.color.BLACK, 12)

arcade.finish_render()

arcade.run()
