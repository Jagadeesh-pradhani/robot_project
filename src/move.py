#!/usr/bin/env python

# Εισαγωγή της βιβλιοθήκης rospy για την επικοινωνία με το ROS
import rospy
# Εισαγωγή του μηνύματος Twist από τη βιβλιοθήκη geometry_msgs.msg
from geometry_msgs.msg import Twist
# Εισαγωγή του μηνύματος LaserScan από τη βιβλιοθήκη sensor_msgs.msg
from sensor_msgs.msg import LaserScan
#Δημιουργία κλάσης RobotController
class RobotController:
    def __init__(self):
        # Αρχικοποίηση του κόμβου ROS με όνομα 'robot_controller'
        rospy.init_node('robot_controller', anonymous=True)
        # Δημιουργία publisher για τις εντολές κίνησης
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # Δημιουργία subscriber για τα δεδομένα σάρωσης laser
        self.laser_subscriber = rospy.Subscriber('/mantzakidisbot/laser/scan', LaserScan, self.laser_callback)
        # Δημιουργία αντικειμένου Twist για τις εντολές κίνησης
        self.twist = Twist()

    def laser_callback(self, data):
        # Επεξεργασία των δεδομένων από το laser για τον εντοπισμό εμποδίων
        # Για ευκολία, θα υποθέσουμε ότι τα δεδομένα laser είναι ένας πίνακας αποστάσεων
        # Εύρεση της ελάχιστης απόστασης από τα δεδομένα laser
        min_distance = min(data.ranges)
        # Έλεγχος εάν υπάρχει εμπόδιο σε κοντινή απόσταση
        if min_distance < 2:  
            # Εάν ανιχνευθεί εμπόδιο, στρίψε
            self.twist.angular.z = 0.5  
        #αν δεν υπάρχει εμπόδιο    
        else:
            # προχώρησε ευθεία
            self.twist.linear.x = 0.2  
            self.twist.angular.z = 0.0
        # publish των εντολών κίνησης
        self.velocity_publisher.publish(self.twist)

    def run(self):
        # Εκκίνηση της εκτέλεσης του κόμβου ROS
        rospy.spin()

if __name__ == '__main__':
    try:
        # Δημιουργία του αντικειμένου της κλάσης RobotController
        controller = RobotController()
        # Έναρξη της εκτέλεσης του κόμβου ROS
        controller.run()
    except rospy.ROSInterruptException:
        pass
