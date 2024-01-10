# Ch 10: This program creates a dynamic illustration of the solar system

import turtle
import math

# Solar System Class
class SolarSystem:
    
    # constructor for solar system
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
        self.ssscreen.tracer(50)
        self.ssscreen.bgcolor("black") # I changed the background color
        
    
    # add a planet to the solar system
    def addPlanet(self, aplanet):
        self.planets.append(aplanet)
    
    # add the sun
    def addSun(self, asun):
        self.thesun = asun
    
    # print all planets
    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)
    
    # stop moving planets
    def freeze(self):
        self.ssscreen.exitonclick()
    
    # move planets 
    def movePlanets(self):
        G = .1 # gravitational constant
        dt = .001 # time step in seconds
        
        for p in self.planets:
            # move the planet based on its current velocity
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())
            
            # get euclidean distance from planet to sun
            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx**2 + ry**2)
            
            # compute x/y acceleration based on force exerted on it by the sun
            accx = G * self.thesun.getMass()*rx/r**3
            accy = G * self.thesun.getMass()*ry/r**3
            
            # compute new velocity based on acceleration
            p.setXVel(p.getXVel() + dt * accx) 
            p.setYVel(p.getYVel() + dt * accy)

# Sun class
class Sun:
    
    # sun constructor
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0
        
        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")
    
    # accessor method for name
    def getName(self):
        return self.name
    
    # accessor method for radius
    def getRadius(self):
        return self.radius
    
    # accessor method for mass
    def getMass(self):
        return self.mass
    
    # accessor method for temperature
    def getTemperature(self):
        return self.temp
    
    # accessor method for volume
    def getVolume(self):
        v = 4.0/3 * math.pi * self.radius**3
        return v
    
    # accessor method for surface area
    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius**2
        return sa
    
    # accessor method for density
    def getDensity(self):
        d = self.mass / self.getVolume()
        return d
    
    # mutator method for name
    def setName(self, newname):
        self.name = newname
    
    # how to print sun
    def __str__(self):
        return self.name
    
    # accessor method for x position
    def getXPos(self):
        return self.x

    # accessor method for y position
    def getYPos(self):
        return self.y


# Planet Class
class Planet:
    
    # planet constructor
    def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic
        
        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x,self.y)
        self.pturtle.down()
    
    # accessor method for name
    def getName(self):
        return self.name
    
    # accessor method for radius
    def getRadius(self):
        return self.radius
    
    # accessor method for mass
    def getMass(self):
        return self.mass
    
    # accessor method for distance
    def getDistance(self):
        return self.distance
    
    # accessor method for volume
    def getVolume(self):
        v = 4.0/3 * math.pi * self.radius**3
        return v
    
    # accessor method for surface area
    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius**2
        return sa
    
    # accessor method for density
    def getDensity(self):
        d = self.mass / self.getVolume()
        return d
    
    # mutator method for name
    def setName(self, newname):
        self.name = newname
    
    # how to display a planet
    def show(self):
        print(self.name)
    
    # how to print planet
    def __str__(self):
        return self.name
    
    # move to new x,y position
    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)
    
    # accessor method for x position
    def getXPos(self):
        return self.x
    
    # accessor method for y position
    def getYPos(self):
        return self.y
    
    # accessor method for x velocity
    def getXVel(self):
        return self.velx
    
    # accessor method for y velocity
    def getYVel(self):
        return self.vely
    
    # mutator method for x velocity
    def setXVel(self, newvx):
        self.velx = newvx
    
    # mutator method for y velocity
    def setYVel(self, newvy):
        self.vely = newvy


# create the solar system and animate it
def createSSandAnimate():
    ss = SolarSystem(2,2)
    
    # Here I wrote a text which indicates that the yellow circle is a sun
    turtle.pencolor("yellow")
    turtle.write("SUN", move=False, align="left", font=("Arial", 25, "normal"))
        
    sun = Sun("SUN", 5000, 10, 5800)
    ss.addSun(sun)
    
    m = Planet("MERCURY", 19.5, 1000, .25, 0, 2, "blue")
    m.setName("EARTH 2.0")
    print( m.getName() )
    ss.addPlanet(m)
    
    m = Planet("EARTH", 47.5, 5000, 0.3, 0, 2.0, "green")
    ss.addPlanet(m)
    
    m = Planet("MARS", 50, 9000, 0.5, 0, 1.63, "red")
    ss.addPlanet(m)
    
    m = Planet("JUPITER", 100, 49000, 0.7, 0, 1, "white")
    ss.addPlanet(m)
    
    # I added Saturn here
    m = Planet("Saturn", 400, 30000, 0.8, 0, 1, "purple")
    ss.addPlanet(m)
    
    m = Planet("Pluto", 1, 500, 0.9, 0, .5, "orange")
    ss.addPlanet(m)
    
    m = Planet("Asteroid", 1, 500, 1.0, 0, .75, "cyan")
    ss.addPlanet(m)
    
    #numTimePeriods = 10000
    #for amove in range(numTimePeriods):
     #   ss.movePlanets()
     
    # I want to keep the simulation running continuously, so I configured it to move indefinitely.
    while True:
        ss.movePlanets()
    ss.freeze()

# main entry point of program:
createSSandAnimate()