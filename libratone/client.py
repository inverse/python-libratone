import socket
import logging

UDP_PORT = 7777


def send_command(device_ip: str, command):
    logging.info(f'Sending to {device_ip} command: {command}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(command, (device_ip, UDP_PORT))
