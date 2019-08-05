import numpy as np
import matplotlib.pyplot as plt

# langton's ant rule
# white cell -> turn right -> move forward
# black cell -> turn left -> move forward

width = 201  # boundary width
height = 201  # boundary height
size = (height, width)  # boundary size

# erase each path: merged @t = 12700, erased @t = 25600
vant = np.matrix(
    [
        [int((height - 1) / 4 * 3), int((width - 1) / 4)],
        [int((height - 1) / 4 * 3), int((width - 1) / 4 * 3)],
    ]
)  # position of ant
vantDirection = [0, 3]  # direction of ant

# build highway early t = 5000
# vant = np.matrix([[int((height-1)/3*2), int((width-1)/4)], [int((height-1)/4*3), int((width-1)/3)]]) #position of ant
# vantDirection = [2, 2] #direction of ant

# build twin highway early t = 5000
# vant = np.matrix([[int((height - 1) / 3 * 2 - 100), int((width - 1) / 4 + 100)],
#                   [int((height - 1) / 4 * 3 - 100), int((width - 1) / 3) + 100]])  # position of ant
# vantDirection = [0, 0] #direction of ant

vectors = np.matrix([[1, 0], [0, -1], [-1, 0], [0, 1]])
# [E, S, W, N]
timeLimit = 13000
simSpan = 500


def move_vant(u, vant, vant_direction):
    u_next = u
    cell = u[vant[:, 0], vant[:, 1]]
    u_next[vant[:, 0], vant[:, 1]] = (u[vant[:, 0], vant[:, 1]] + 1) % 2
    if cell == 0:
        vant_direction = (vant_direction + 1) % 4
    else:
        vant_direction = (vant_direction - 1) % 4
    vant = vant + vectors[vant_direction, :]
    vant[:, 0] = vant[:, 0] % height
    vant[:, 1] = vant[:, 1] % width
    # print(vant)
    return (u_next, vant, vant_direction)


# initial field
U = np.random.randint(2, size=size)  # np.zero(size) -> something went wrong

fig = plt.figure()
ax = fig.add_subplot(111)
img = ax.imshow(U, interpolation="nearest", cmap=plt.cm.Greys)
U = np.zeros(size, dtype=np.int)  # reset U
i = 0
while i < timeLimit:
    (U, vant[0], vantDirection[0]) = move_vant(U, vant[0], vantDirection[0])
    (U, vant[1], vantDirection[1]) = move_vant(U, vant[1], vantDirection[1])
    img.set_data(U)
    i += 1
    ax.set_title("t = {}".format(i))
    if i > timeLimit - simSpan:
        plt.pause(0.0001)
plt.show()
