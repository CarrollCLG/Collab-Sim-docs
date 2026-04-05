import bpy
import socket
import threading

SOCKET_HOST = "localhost"
SOCKET_PORT = 9876

new_lines_queue = []
queue_lock = threading.Lock()

def socket_server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((SOCKET_HOST, SOCKET_PORT))
    srv.listen(5)
    srv.settimeout(1.0)
    print("SCRN_01: socket server running on port 9876")
    while True:
        try:
            conn, addr = srv.accept()
            data = b""
            while True:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                data += chunk
            msg = data.decode("utf-8").strip()
            if msg:
                with queue_lock:
                    new_lines_queue.append(msg)
                print(f"SCRN_01: received: {msg[:50]}")
            conn.close()
        except socket.timeout:
            continue
        except Exception as e:
            print(f"SCRN_01 socket error: {e}")
            break

def init(cont):
    cont.owner["initialized"] = True
    cont.owner["count"] = 0
    print("SCRN_01: initialized")
    t = threading.Thread(target=socket_server, daemon=True)
    t.start()

def update(cont):
    own = cont.owner
    if not own.get("initialized", False):
        return

    with queue_lock:
        incoming = list(new_lines_queue)
        new_lines_queue.clear()

    if not incoming:
        return

    own["count"] += len(incoming)
    print(f"SCRN_01: got {len(incoming)} messages, total={own['count']}")

    try:
        img = bpy.data.images["scrn01_tex"]
        w, h = img.size[0], img.size[1]
        pixels = [0.0, 0.3, 0.0, 1.0] * (w * h)
        img.pixels = pixels
        img.update()
        print("SCRN_01: painted green successfully")
    except Exception as e:
        print(f"SCRN_01: paint failed: {e}")
