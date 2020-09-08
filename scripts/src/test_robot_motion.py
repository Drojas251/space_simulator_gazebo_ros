#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg 
import copy
from std_msgs.msg import String


import rospkg, genpy
import yaml



def move_gripper(value):
	gripper_values = gripper.get_current_joint_values()
	print "============ Joint values: ", gripper_values

        gripper_values[0] = value
        gripper_values[1] = - value
        gripper_values[2] = value
        gripper_values[3] = value
        gripper_values[4] = - value
        gripper_values[5] = value

	print( " ")
	print "============ Joint values: ", gripper_values
 
	
	gripper.set_joint_value_target(gripper_values)
	plan_open = gripper.plan()
	rospy.sleep(1)
	gripper.execute(plan_open)
	gripper.set_start_state_to_current_state()
	arm_group.set_start_state_to_current_state() 
	
def move_rail (value):
	rail_values = rail.get_current_joint_values()
	rail_values[0] = value

	rail.set_joint_value_target(rail_values)	
	plan_open = rail.plan()
	rospy.sleep(1)
	rail.execute(plan_open)
	rail.set_start_state_to_current_state()


def get_right_bolt():

	current_pose = arm_group.get_current_pose().pose
	x=current_pose.orientation.x
	y = current_pose.orientation.y
	z = current_pose.orientation.z
	w =current_pose.orientation.w

	pose_target = geometry_msgs.msg.Pose()

	pose_target.orientation.w = w
	pose_target.orientation.x = x
	pose_target.orientation.y = y
	pose_target.orientation.z = z

	pose_target.position.x = 0.4
	pose_target.position.y = 0.45
	pose_target.position.z =0.35

	arm_group.set_pose_target(pose_target)


	pose_target.position.z = 0.165
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	move_gripper(0.40)
	rospy.sleep(2)

	pose_target.position.z = 0.35
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()


	pose_target.position.x = 0.4
	pose_target.position.y = 0.18	
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	pose_target.position.z = 0.26
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	rospy.sleep(1)
	move_gripper(0.0)

	pose_target.position.z = 0.3
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()


	arm_group.set_start_state_to_current_state()
	arm_group.stop()

def get_3D_part():

	current_pose = arm_group.get_current_pose().pose
	x=current_pose.orientation.x
	y = current_pose.orientation.y
	z = current_pose.orientation.z
	w =current_pose.orientation.w

	pose_target = geometry_msgs.msg.Pose()

	pose_target.orientation.w = w
	pose_target.orientation.x = x
	pose_target.orientation.y = y
	pose_target.orientation.z = z

	pose_target.position.x = 0.0
	pose_target.position.y = 0.35
	pose_target.position.z =0.6

	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	pose_target.position.y = 0.65
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()


	pose_target.position.z = 0.568
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	move_gripper(0.40)
	rospy.sleep(2)

	pose_target.position.z = 0.6
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()


	pose_target.position.x = 0.0
	pose_target.position.y = 0.35	
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()


	arm_group.set_start_state_to_current_state()
	arm_group.stop()

def place_3D_part():

	pose_target = geometry_msgs.msg.Pose()

        pose_target.orientation.w = 0.7071266782625533
	pose_target.orientation.x = -0.7070867388134034
	pose_target.orientation.y = 0.0003319606955996503
	pose_target.orientation.z = -0.0003073852465376433

	pose_target.position.x = 0.25
	pose_target.position.y = 0.25
	pose_target.position.z = 0.32
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	pose_target.position.x = 0.4
	pose_target.position.y = 0.15
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	pose_target.position.y = 0.0
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()



	pose_target.position.z = 0.25
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	rospy.sleep(1)
	move_gripper(0.0)


	arm_group.set_start_state_to_current_state()
	arm_group.stop()

def test_motion():

	current_pose = arm_group.get_current_pose().pose
	x=current_pose.orientation.x
	y = current_pose.orientation.y
	z = current_pose.orientation.z
	w =current_pose.orientation.w

	pose_target = geometry_msgs.msg.Pose()

	pose_target.orientation.w = w
	pose_target.orientation.x = x
	pose_target.orientation.y = y
	pose_target.orientation.z = z

	pose_target.position.x = -1.25
	pose_target.position.y = 0.5
	pose_target.position.z =0.55

	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	pose_target.position.z =0.47

	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

	arm_group.set_start_state_to_current_state()
	arm_group.stop()



moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous =True)
scene = moveit_commander.PlanningSceneInterface()
robot = moveit_commander.RobotCommander()

arm_group = moveit_commander.MoveGroupCommander("manipulator")
gripper = moveit_commander.MoveGroupCommander("hand")
rail = moveit_commander.MoveGroupCommander("rail")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

end_effector_link = arm_group.get_end_effector_link()



arm_group.set_named_target("start")
plan1 = arm_group.go()
move_rail(0.0)

arm_group.set_named_target("3D_printer_grasp")
plan1 = arm_group.go()


move_gripper(0.0)

get_3D_part()


move_rail(-1.25)

test_motion()

move_gripper(0.0)

arm_group.set_named_target("3D_printer_grasp")
plan1 = arm_group.go()









rospy.sleep(3)
moveit_commander.roscpp_shutdown()
