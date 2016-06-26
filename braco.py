'''
Created on 23/04/2015

@author: philippeoz
'''

import OpenGL
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv
from random import uniform
from OpenGL.raw.GLU import gluPerspective

elbow = 0
hand = 0
fingers =0
polegar =0
indicador =0
medio=0
horizontal = 0

def display():
    global elbow, hand, fingers, polegar, indicador, medio, horizontal
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef (0.0, 2.6, 0.0)
    glPushMatrix()
    glColor3f(0.7, 0.7, 0.7)
    glScalef (5.6, 0.4, 0.4)
    glutSolidCube (1.0)
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()


    glTranslatef (horizontal, 2.5, 0.0)


    glTranslatef (0.0, -1.0, 0.0)
    glPushMatrix()
    glColor3f(0.4, 0.0, 0.0)
    glScalef (0.4, 2.0, 0.4)
    glutSolidCube(1.0)
    glPopMatrix()

    glTranslatef (0.0, -1.0, 0.0)
    glRotatef (elbow, 0.0, 0.0, 1.0)
    glColor3f(0.4, 0.0, 0.0)
    glutSolidSphere(0.26, 50, 50)
    glTranslatef (0.0, -1.0, 0.0)
    glPushMatrix()
    glColor3f(0.4, 0.0, 0.0)
    glScalef (0.4, 2.0, 0.4)
    glutSolidCube (1.0)
    glPopMatrix()

    glTranslatef (0.0, -0.6, 0.0)
    glRotatef (hand, 0.0, 1.0, 0.0)
    glTranslatef (0.0, -0.6, 0.0)
    glPushMatrix()
    glColor3f(0.5, 0.0, 0.0)
    glScalef (0.6, 0.3, 0.6)
    glutSolidSphere(0.70, 50, 50)
    #glutSolidCube (1.0)
    glPopMatrix()


    glPushMatrix()

    glPushMatrix()
    glTranslatef (-0.2, -0.05, 0.0)
    glRotatef (((fingers*(-1))+indicador), 0.0, 0.0, 1.0)
    glTranslatef (-0.2, -0.3, 0.0)
    glPushMatrix()
    glColor3f(0.7, 0.1, 0.7)
    glScalef (0.2, 0.6, 0.2)
    glutSolidCube (1.0)
    glPopMatrix()
    glPopMatrix()
    

    glPushMatrix()
    glTranslatef (0.2, -0.05, -0.15)
    glRotatef ((fingers+medio), 0.0, 0.0, 1.0)
    glTranslatef (0.15, -0.3, -0.15)
    glPushMatrix()
    glColor3f(0.7, 0.1, 0.3)
    glScalef (0.2, 0.6, 0.2)
    glutSolidCube (1.0)
    glPopMatrix()
    glPopMatrix()


    glPushMatrix()
    glTranslatef (0.2, -0.05, 0.15)
    glRotatef ( (fingers+polegar), 0.0, 0.0, 1.0)
    glTranslatef (0.15, -0.3, 0.15)
    glPushMatrix()
    glColor3f(0.5, 0.7, 0.4)
    glScalef (0.2, 0.6, 0.2)
    glutSolidCube (1.0)
    glPopMatrix()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()
    glutSwapBuffers()

def reshape (w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0,w / h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef (0.0, 0.0, -5.0)

def keyboard (key, x, y):
    global elbow, hand, fingers, polegar, indicador, medio, horizontal
    if key == 'o':
        if horizontal < 2.5:
            horizontal = horizontal + 0.1
        glutPostRedisplay()
    elif key == 'O':
        if horizontal > -2.5:
            horizontal = horizontal - 0.1
        glutPostRedisplay()
    elif key == 'c':
        if elbow != 110:
            elbow = (elbow + 5) % 360
        glutPostRedisplay()
    elif key == 'C':
        if elbow != 250:
            elbow = (elbow - 5) % 360
        glutPostRedisplay()
    elif key == 'H':
        hand = (hand + 5) % 360
        glutPostRedisplay()
    elif key == 'h':
        hand = (hand - 5) % 360
        glutPostRedisplay()
    elif key == 'U':
        if fingers != 30:
            fingers = (fingers + 5) % 360
        polegar = 0
        medio = 0
        indicador = 0
        glutPostRedisplay()
    elif key == 'u':
        if fingers != 290:
            fingers = (fingers - 5) % 360
        polegar = 0
        medio = 0
        indicador = 0
        glutPostRedisplay()
    elif key == 'p':
        if polegar != 290:
            polegar = (polegar - 5) % 360
        fingers = 0
        glutPostRedisplay()
    elif key == 'P':
        if polegar != 30:
            polegar = (polegar + 5) % 360
        fingers = 0
        glutPostRedisplay()
    elif key == 'i':
        if indicador != 90:
            indicador = (indicador + 5) % 360
        fingers = 0
        glutPostRedisplay()
    elif key == 'I':
        if indicador != 330:
            indicador = (indicador - 5) % 360
        fingers = 0
        glutPostRedisplay()
    elif key == 'm':
        if medio != 295:
            medio = (medio - 5) % 360
        fingers = 0
        glutPostRedisplay()
    elif key == 'M':
        if medio != 25:
            medio = (medio + 5) % 360
        fingers = 0
        glutPostRedisplay()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Braco PyOpenGL     @PhilippeOz")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    #glutMouseFunc(mouse)
    #glutMotionFunc(mouse)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()