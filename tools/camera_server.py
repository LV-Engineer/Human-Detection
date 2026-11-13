import cv2
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

cap = cv2.VideoCapture(0)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "multipart/x-mixed-replace; boundary=frame")
        self.end_headers()
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            _, jpg = cv2.imencode(".jpg", frame)
            self.wfile.write(b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpg.tobytes() + b"\r\n")


ThreadingHTTPServer(("127.0.0.1", 5000), Handler).serve_forever()