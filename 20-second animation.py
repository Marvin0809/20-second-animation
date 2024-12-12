import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("20-second animation with two (2) textured objects")

glEnable(GL_DEPTH_TEST)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -22)
glRotatef(90, 1, 0, 0)

def add_texture(image_file):
    image = pygame.image.load(image_file)
    data = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

def draw_cube():
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(-1, 1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, -1)
    glTexCoord2f(0, 1)
    glVertex3f(1, -1, -1)
    glTexCoord2f(0, 0)
    glVertex3f(-1, 1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(-1, 1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, 1, -1)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, -1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, -1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(-1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, -1)
    glEnd()

def draw_sphere(radius=1, slices=20, stacks=20):
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, slices, stacks)

angle_orbit = 0
orbit_speed = 360 / 20
radius_cube = 5
radius_sphere = 8
add_texture('texture.png')

start_time = pygame.time.get_ticks()

while pygame.time.get_ticks() - start_time < 20000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    angle_orbit = ((pygame.time.get_ticks() - start_time) / 20000) * 360

    glPushMatrix()
    glTranslatef(math.cos(math.radians(angle_orbit)) * radius_cube, 0, math.sin(math.radians(angle_orbit)) * radius_cube)
    glRotatef(angle_orbit, 1, 1, 0)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(math.cos(math.radians(angle_orbit + 180)) * radius_sphere, 0, math.sin(math.radians(angle_orbit + 180)) * radius_sphere)
    glRotatef(angle_orbit, 0, 1, 0)
    draw_sphere()
    glPopMatrix()

    glPopMatrix()

    pygame.display.flip()

    pygame.time.wait(15)

pygame.quit()
