import rospy
import smach

from zordon_tts.srv import Tts

class Say(smach.State):
    
    def __init__(self, sentence):
        smach.State.__init__(self, outcomes=["spoken"])
        self._sentence = sentence
        self._service = rospy.ServiceProxy('/zordon/tts', Tts)

    def execute(self, userdata=None):
        if not self._sentence:
            rospy.logerr("Not saying anything")
            return "spoken"
        self._service(self._sentence)
        return "spoken"
