from app import app
import leancloud

application = app
application = leancloud.HttpsRedirectMiddleware(application)