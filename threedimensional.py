import pygame
import consts
import math
import random
class Point3D:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Point2D:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y

class Edge:
    def __init__(self, i1,i2) -> None:
        self.i1 = i1
        self.i2 =i2

class Renderer3D:
    def __init__(self, points, edges, screen):
        self.points3D = points
        self.edges = edges
        self.FOV = 256
        self.screen = screen
        self.colour = (0,128,0)
    def project(self, point3d):
        return Point2D((consts.WIDTH/2) + (point3d.x* self.FOV) / (point3d.z + self.FOV) , (consts.HEIGHT/2) + (point3d.y * self.FOV)/(point3d.z + self.FOV) )
    def render(self):
        self.screen.fill((0,0,0))
        for edge in self.edges:
            p12d = self.project(self.points3D[edge.i1])
            p22d = self.project(self.points3D[edge.i2])
            pygame.draw.line(self.screen, self.colour, (p12d.x, p12d.y), (p22d.x, p22d.y), consts.THICKNESS)
        pygame.display.flip()
    def rotateX(self, point3d):
        returnPoint = Point3D(0,0,0)
        returnPoint.x = point3d.x
        returnPoint.y = math.cos(consts.ROT) * point3d.y - math.sin(consts.ROT) * point3d.z
        returnPoint.z = math.sin(consts.ROT) * point3d.y + math.cos(consts.ROT) * point3d.z
        return returnPoint
    def rotateY(self, point3d):
        returnPoint = Point3D(0,0,0)
        returnPoint.x = math.cos(consts.ROT) * point3d.x - math.sin(consts.ROT) * point3d.z
        returnPoint.y = point3d.y
        returnPoint.z = math.sin(consts.ROT) * point3d.x + math.cos(consts.ROT) * point3d.z
        return returnPoint


