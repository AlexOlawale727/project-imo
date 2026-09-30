
import http.server
import socketserver
import json
import os

PORT = 8080

# Socratic Knowledge Base mapped to specific topics
SOCRATIC_KNOWLEDGE_BASE = {
    "ohm": {
        "concept": "Ohm's Law (V = IR)",
        "prompt": "Ohm's Law connects Voltage (V), Current (I), and Resistance (R). If you keep voltage constant but double the resistance, what happens to the electric current?"
    },
    "photosynthesis": {
        "concept": "Photosynthesis",
        "prompt": "Photosynthesis is how green plants produce glucose. What gas do plants take in from the air to make this happen, and what gas do they release for us to breathe?"
    },
    "velocity": {
        "concept": "Velocity & Motion",
        "prompt": "Velocity is speed with direction. If a car moves around a circular track at a steady 50 km/h, why is its velocity still changing?"
    },
    "pythagoras": {
        "concept": "Pythagoras Theorem (a² + b² = c²)",
        "prompt": "In a right-angled triangle with sides 3 and 4, how would you set up the equation to find the hypotenuse (longest side)?"
    }
}

DEFAULT_PROMPT = "That is a great question! Before we break it down together, what do you already know about this concept or topic?"

def generate_socratic_response(user_query):
    query_lower = user_query.lower()
   
    # Check for topic keywords
    for key, data in SOCRATIC_KNOWLEDGE_BASE.items():
        if key in query_lower:
            return f"<strong>[{data['concept']}]</strong><br>{data['prompt']}"
           
    # Universal fallback for unindexed topics
    return DEFAULT_PROMPT

class ImoRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
           
            try:
                data = json.loads(post_data.decode('utf-8'))
                user_msg = data.get('message', '')
               
                bot_reply = generate_socratic_response(user_msg)
               
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
               
                response_payload = json.dumps({'reply': bot_reply})
                self.wfile.write(response_payload.encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_error(404, "Endpoint not found")

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with socketserver.TCPServer(("", PORT), ImoRequestHandler) as httpd:
        print(f"🧠 Project Ìmọ̀ Node Server Running on Port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
