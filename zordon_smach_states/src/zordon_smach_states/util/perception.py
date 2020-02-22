import rospy

from std_msgs.msg import Empty

class Perception():
    def __init__(self):
        rospy.loginfo("Perception init()")
        self.sub = rospy.Subscriber("/zordon/perception", Empty, self._callback)

        self.operator_id = 0
    def _callback(self, msg):
        rospy.loginfo("Perception callback()")
