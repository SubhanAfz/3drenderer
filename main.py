import consts
import threedimensional
import pygame
import random
clock = pygame.time.Clock()

screen = pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))

#Cube
#points = [threedimensional.Point3D(0,0,0), threedimensional.Point3D(0,50,0), threedimensional.Point3D(50,0,0), threedimensional.Point3D(50,50,0), threedimensional.Point3D(0,0,50), threedimensional.Point3D(0,50,50), threedimensional.Point3D(50,0,50), threedimensional.Point3D(50,50,50)]
#edges = [threedimensional.Edge(0, 1), threedimensional.Edge(0, 2), threedimensional.Edge(0, 4), threedimensional.Edge(1,3), threedimensional.Edge(1, 5), threedimensional.Edge(2, 6), threedimensional.Edge(2, 3), threedimensional.Edge(3, 7), threedimensional.Edge(4, 5), threedimensional.Edge(4, 6), threedimensional.Edge(5, 7), threedimensional.Edge(7, 6)]


#square based pyramid
points = [threedimensional.Point3D(0,0,0), threedimensional.Point3D(0,50,0), threedimensional.Point3D(50,0,0), threedimensional.Point3D(50,50,0), threedimensional.Point3D(25,25,50)]
edges = [threedimensional.Edge(0,1), threedimensional.Edge(0,2), threedimensional.Edge(0,4), threedimensional.Edge(1,4), threedimensional.Edge(1,3), threedimensional.Edge(3,4), threedimensional.Edge(3,2), threedimensional.Edge(2,4)]

renderer = threedimensional.Renderer3D(points, edges, screen)

running = True
while running:
    clock.tick(20)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    newPoint3d = []
    for point in renderer.points3D:
        newpoint = renderer.rotateX(point)
        newPoint3d.append(newpoint)
        print(newpoint.x, newpoint.y, newpoint.z)
        print(point.x, point.y, point.z)
    renderer.points3D = newPoint3d
    renderer.colour = (0,128,0)
    renderer.render()