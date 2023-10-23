import imageio

filesnames=["r1.jpg","r2.jpg","r3.jpg"]

images=[]
for filename in filesnames:
    images.append(imageio.imread(filename))
imageio.mimsave("RS.gif",images,"GIF",duration=1)