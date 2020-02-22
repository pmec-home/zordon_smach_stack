import rospy
import smach

from zordon_nlu.srv import Nlu
from std_srvs.srv import Trigger, Empty

class ListenWakeWord(smach.State):

    def __init__(self, outcomes=["listened"]):
        self._service = rospy.ServiceProxy('/zordon/wake_word', Empty)

    def execute(self, userdata=None):
        self._service()
        return "listened"

class ListenStt(smach.State):
    def __init__(self, outcomes=["listened", "not_listened"], output_keys=['output_text']):
        self._service = rospy.ServiceProxy('/zordon/stt', Trigger)

    def execute(self, userdata):
        res = self._service()
        if not res.success:
            return "not_listened"
        userdata.output_text = res.message
        return "listened"


class ListenNlu(smach.State):
    def __init__(self, outcomes=["understood", "not_understood"],
                        input_keys=["input_text"],
                        output_keys=["message", "intent", "entities"]):
        self._service = rospy.ServiceProxy('/zordon/nlu', Nlu)

    def execute(self, userdata):
        res = self._service(usedata.input_text)
        if(res.intent == "fallback"):
            return "not_understood"
        usedata.message  = res.message
        usedata.intent   = res.intent
        usedata.entities = res.entities
        return "understood"

