from mcpi.minecraft import Minecraft
import mcpi.block as block 

mc = Minecraft.create()

a_prime_ground = (-443, 70, 369)
width = 19
depth = 25
height = 5

#clear the floor
mc.setBlocks(a_prime_ground[0], a_prime_ground[1] - 1, a_prime_ground[2], 
             a_prime_ground[0] + width, a_prime_ground[1] - 1, a_prime_ground[2] + depth, 0)
# floor
mc.setBlocks(a_prime_ground[0], a_prime_ground[1] - 1, a_prime_ground[2], 
             a_prime_ground[0] + width, a_prime_ground[1] - 1, a_prime_ground[2] + depth, 5)


 # loop it for multifloor
             
for floor in range(5):
    a_prime = (a_prime[0], a_prime_ground[1] + floor * 6, a_prime[2])

    # # clear whole floor
    mc.setBlocks(a_prime[0], a_prime[1] + 1, a_prime[2], 
                a_prime[0] + width, a_prime[1] + height + 1, a_prime[2] + depth, 0)

    # wall_1_1 
    mc.setBlocks(a_prime[0], a_prime[1], a_prime[2], 
                a_prime[0], a_prime[1] + height, a_prime[2] + depth, 5)

    # wall_1_2
    mc.setBlocks(a_prime[0] + 7, a_prime[1], a_prime[2], 
                a_prime[0] + 7, a_prime[1] + height, a_prime[2] + depth, 5)

    # wall_1_3
    mc.setBlocks(a_prime[0] + 7 + 5, a_prime[1], a_prime[2], 
                a_prime[0] + 7 + 5, a_prime[1] + height, a_prime[2] + depth, 5)

    # wall_1_4
    mc.setBlocks(a_prime[0] + 7 + 5 + 7, a_prime[1], a_prime[2], 
                a_prime[0] + 7 + 5 + 7, a_prime[1] + height, a_prime[2] + depth, 5)

    # wall_2_1
    mc.setBlocks(a_prime[0], a_prime[1], a_prime[2], 
                a_prime[0] + 7 + 5 + 7, a_prime[1] + height, a_prime[2], 5)

    # wall_2_2
    mc.setBlocks(a_prime[0], a_prime[1], a_prime[2] + depth, 
                a_prime[0] + 7 + 5 + 7, a_prime[1] + height, a_prime[2] + depth, 5)


                

    # roof
    mc.setBlocks(a_prime[0], a_prime[1] + height + 1, a_prime[2], 
                a_prime[0] + width, a_prime[1] + height + 1, a_prime[2] + depth, 5)

    # Lights
    light_pos_x = a_prime[0] + 1

    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + depth - 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 10 + 1, block.GLOWSTONE_BLOCK)

    light_pos_x =light_pos_x + 5
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + depth - 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 10 + 1, block.GLOWSTONE_BLOCK)

    light_pos_x =light_pos_x + 2
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + depth - 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 10 + 1, block.GLOWSTONE_BLOCK)

    light_pos_x =light_pos_x + 3
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + depth - 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 10 + 1, block.GLOWSTONE_BLOCK)

    light_pos_x =light_pos_x + 2
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + depth - 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 10 + 1, block.GLOWSTONE_BLOCK)

    light_pos_x =light_pos_x + 5
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + depth - 1, block.GLOWSTONE_BLOCK)
    mc.setBlock(light_pos_x, a_prime[1] + height, a_prime[2] + 10 + 1, block.GLOWSTONE_BLOCK)
