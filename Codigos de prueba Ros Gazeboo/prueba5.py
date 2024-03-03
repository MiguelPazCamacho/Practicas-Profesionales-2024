import rclpy
from geometry_msgs.msg import Pose

def main():
    rclpy.init()

    node = rclpy.create_node('object_controller')

    # Publicar en el tópico de posición del objeto
    publisher = node.create_publisher(Pose, '/model/vehicle_blue/pose', 10)

    # Crear un mensaje Pose para establecer la nueva posición del objeto
    pose_msg = Pose()
    pose_msg.position.x = 6.0   # Nueva posición en el eje x
    pose_msg.position.y = 0.0   # Nueva posición en el eje y
    pose_msg.position.z = 0.325  # Nueva posición en el eje z

    # Publicar el mensaje para mover el objeto
    publisher.publish(pose_msg)
    print("publicado")

    # Esperar un poco para que se procese el mensaje
    rclpy.spin_once(node, timeout_sec=1)

    # Cerrar el nodo
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
