#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot #Import a base Robot

class EuhBot (Robot): 
    def init (self):
        self.setColor(255, 36, 0)
        self.setGunColor(255, 215, 0)
        self.setRadarColor(255, 36, 0)
        self.setBulletsColor(255, 36, 0)
        
        size = self.getMapSize() 
        self.radarVisible(True) 
        self.lockRadar("gun")
        
    def run (self):
        self.gunTurn(5)
        pass
    
    def sensors (self): 
        pos = self.getPosition() 
        x = pos.x() 
        y = pos.y() 
        
        angle = self.getGunHeading() 
        angle = self.getHeading() 
        angle = self.getRadarHeading() 
        list = self.getEnemiesLeft() 
        for robot in list:
            id = robot["id"]
            name = robot["name"]
        
    def onHitByRobot (self, robotId, robotName):
        self.rPrint("damn a bot collided me!")

    def onHitWall (self):
        pass
    
    def onRobotHit (self, robotId, robotName): 
        self.rPrint('collision with:' + str(robotName)) 
       
    def onHitByBullet (self, bulletBotId, bulletBotName, bulletPower): 
        self.reset()  
        self.rPrint("hit by " + str(bulletBotName) + "with power:" +
                     str(bulletPower))
        
    def onBulletHit (self, botId, bulletId):
        self.rPrint("fire done on " +str( botId))
                    
    def onBulletMiss (self, bulletId):
        self.rPrint("the bullet "+ str(bulletId) + " fail")
        
    def onRobotDeath (self):
        self.rPrint("damn I'm Dead")
    
    def onTargetSpotted (self, botId, botName, botPos):
        if (self.isEnemy(botName)):
            self.fire(10)

        self.rPrint("I see the bot:" + str(botId) + "on position: x:"
                    + str(botPos.x()) + " , y:" + str(botPos.y()))

    def isEnemy (self, botName):
        botName == "EuhBot"
