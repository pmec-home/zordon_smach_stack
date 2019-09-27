import rospy
import smach

import zordon_smach_states as states

def main():
    rospy.init_node("teste")

    sm = smach.StateMachine(outcomes=['done'])

    with sm:
        smach.StateMachine.add('Say', states.Say("Hello World!"), transitions={'spoken':'done'})

    outcome = sm.execute()

if __name__ == '__main__':
    main()
