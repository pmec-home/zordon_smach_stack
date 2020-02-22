import rospy
import smach

import zordon_smach_states as states

def main():
    rospy.init_node("teste")

    sm = smach.StateMachine(outcomes=['done'])

    with sm:
        smach.StateMachine.add('say_moving', states.Say("Moving to the meeting point"), transitions={'spoken':'say_play_rides'})
        smach.StateMachine.add('say_play_rides',  states.Say("I want to play riddles"), transitions={'spoken':'say_play_rides'})
    outcome = sm.execute()

if __name__ == '__main__':
    main()
