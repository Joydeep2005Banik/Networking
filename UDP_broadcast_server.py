import netpack as npk
import time

broadcast_ip_1 = '172.20.255.255'
client_port = 6969
addr = (broadcast_ip_1, client_port)

# Step-1
server_socket = npk.create_udp_broadcast_server_socket()

while True:
    try:
        data = "Yoo !!! Joydeep this side :)"
        npk.send_data_to_udp_client(server_socket, data, addr)
        print("[SENT] Broadcast Message")
        time.sleep(2)
    except KeyboardInterrupt:
        print('Program Interrupted')
        npk.send_data_to_udp_client(server_socket, 'close', addr)
        npk.close_socket_connection(server_socket)
        break
