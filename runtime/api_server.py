from __future__ import annotations

from urllib.parse import urlparse

try:
    from server import Handler as HomeHubHandler
    from server import RUNTIME_HOST, RUNTIME_PORT, ThreadingHTTPServer, run_background_email_sync, threading
except ModuleNotFoundError:
    from runtime.server import Handler as HomeHubHandler
    from runtime.server import RUNTIME_HOST, RUNTIME_PORT, ThreadingHTTPServer, run_background_email_sync, threading


class ApiOnlyHandler(HomeHubHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self._send_json(
                {
                    "ok": True,
                    "service": "homehub-api",
                    "mode": "api-only",
                    "health": "/api/health",
                }
            )
            return
        if not parsed.path.startswith("/api/"):
            self.send_error(404)
            return
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        if not parsed.path.startswith("/api/"):
            self.send_error(404)
            return
        super().do_POST()


if __name__ == "__main__":
    email_sync_thread = threading.Thread(target=run_background_email_sync, daemon=True)
    email_sync_thread.start()
    server = ThreadingHTTPServer((RUNTIME_HOST, RUNTIME_PORT), ApiOnlyHandler)
    print(f"HomeHub API started at http://{RUNTIME_HOST}:{RUNTIME_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHomeHub API stopped")
        server.server_close()
