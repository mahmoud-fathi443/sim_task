import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import math


class PointsDistance(Node):
    def __init__(self):
        super().__init__("points_distance")
        self.point1_subscription = self.create_subscription(PointStamped, 'point1_topic', self.point1_callback, 10)
        self.point2_subscription = self.create_subscription(PointStamped, 'point2_topic', self.point2_callback, 10)

        self.point1 = PointStamped()
        self.point2 = PointStamped()

        self.timer_ = self.create_timer(1, self.timer_callback)

    def point1_callback(self, msg):
        self.point1 = msg
    def point2_callback(self, msg):
        self.point2 = msg

    def timer_callback(self):
        x1 = self.point1.point.x
        y1 = self.point1.point.y
        z1 = self.point1.point.z
        x2 = self.point2.point.x
        y2 = self.point2.point.y
        z2 = self.point2.point.z

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        self.get_logger().info(f"Distance between points: {distance}")

def main(args=None):
    rclpy.init(args=args)
    pointsDistance = PointsDistance()
    rclpy.spin(pointsDistance)
    pointsDistance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
