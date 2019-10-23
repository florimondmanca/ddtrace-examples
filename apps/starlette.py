from ddtrace import tracer
from ddtrace_asgi.middleware import TraceMiddleware
from starlette.responses import PlainTextResponse

app = PlainTextResponse("OK")
app = TraceMiddleware(app, tracer, service="tracing-example-starlette")
