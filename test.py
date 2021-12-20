green_array = pygame.surfarray.pixels_green(screen)
blue_array = pygame.surfarray.pixels_blue(screen)
red_array = pygame.surfarray.pixels_red(screen) 
green_array1 = green_array
blue_array1 = blue_array
red_array1 = red_array
# b[(a, b)] = (a1, b1)
# (a1, b1) - (a, b) - 8
pygame.surface.fill(screen, c.sky_color)
for i in array:
    green_array[b[i]] = green_array1[i]
    blue_array[b[i]] = blue_array1[i]
    red_array[b[i]] = red_array1[i] 
