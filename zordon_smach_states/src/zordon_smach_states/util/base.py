import rospy
import tf

from geometry_msgs.msg import PoseStamped

class Base():

    def __init__(self):
        self.tf_listener = TransformListener()

    def get_location(self):

        try:
            time = rospy.Time.now()
            self.tf_listener.waitForTransform("/map", "/Zordon_base", time, rospy.Duration(20.0))
            (ro_trans, ro_rot) = self.tf_listener.lookupTransform("/map", "/Zordon_base", time)

            position = geometry_msgs.msg.Point()
            orientation = geometry_msgs.msg.Quaternion()

            position.x = ro_trans[0]
            position.y = ro_trans[1]
            orientation.x = ro_rot[0]
            orientation.y = ro_rot[1]
            orientation.z = ro_rot[2]
            orientation.w = ro_rot[3]

            target_pose = geometry_msgs.msg.PoseStamped(pose=geometry_msgs.msg.Pose(position=position, orientation=orientation))
            target_pose.header.frame_id = "/map"
            target_pose.header.stamp = time
            return target_pose

        except (tf.LookupException, tf.ConnectivityException) as e:
            rospy.logerr("tf request failed!, {}".format(e))
            target_pose = geometry_msgs.msg.PoseStamped(pose=geometry_msgs.msg.Pose(position=position, orientation=orientation))
            target_pose.header.frame_id = "/map"
            return target_pose

