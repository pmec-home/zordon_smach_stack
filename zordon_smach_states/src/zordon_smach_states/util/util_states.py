import rospy
import smach
import time

class Wait(smach.State):
    
    def __init__(self, seconds):
        smach.State.__init__(self, outcomes=["complete"])
        self._seconds = seconds

    def execute(self, userdata=None):
        time.sleep(self._seconds)
        return "complete"