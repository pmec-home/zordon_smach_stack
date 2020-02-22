import rospy

from perception import *

class Robot():
    def __init__(self):
        rospy.loginfo("Robot init()")
        self.perception = Perception()
        self.base = Base()
