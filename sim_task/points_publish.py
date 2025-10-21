import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped

class PointPublish(Node):
    def __init__(self):
        super().__init__("points_publish")
        self.point1_publisher_ = self.create_publisher(PointStamped, 'point1_topic', 10)
        self.point2_publisher_ = self.create_publisher(PointStamped, 'point2_topic', 10)
        self.timer_ = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        point1 = PointStamped()
        point2 = PointStamped()

        point1.header.frame_id = "map"
        point1.header.stamp = self.get_clock().now().to_msg()
        point1.point.x = 1.0
        point1.point.y = 1.0
        point1.point.z = 1.0

        point2.header.frame_id = "map"
        point2.header.stamp = self.get_clock().now().to_msg()
        point2.point.x = 2.0
        point2.point.y = 3.0
        point2.point.z = 0.5
        
        self.point1_publisher_.publish(point1)
        self.point2_publisher_.publish(point2)
        self.get_logger().info(f"Published Point1: ({point1.point.x}, {point1.point.y}, {point1.point.z})")
        self.get_logger().info(f"Published Point2: ({point2.point.x}, {point2.point.y}, {point2.point.z})")


def main(args=None):
    rclpy.init(args=args)
    pointPublish = PointPublish()
    rclpy.spin(pointPublish)
    pointPublish.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


        