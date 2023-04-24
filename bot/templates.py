START_MESSAGE = """
Welcome to the FA Notificator. This bot will send you notifications once in a while from the Furaffinity.
"""

HELP_MESSAGE = """
The 'a' and 'b' cookies needed to check your FA notifications. It would be stored in a private way and used to fetch notifications only.\n\n
How to get your FA cookies: http://localhost/ \n
Command template: /cookie <a:cookie> <b:cookie>\n
Command example: /cookie aitd-ayoa-awoi-1232 aw62-w872-98mn-oiy6
"""

COOKIE_SUCCESS_MESSAGE = """
Your cookies are stored and the notification information successfully fetched. Your notification journey begins.
"""

COOKIE_ERROR_MESSAGE = """
Invalid cookies. See /help and try again.
"""

INTERVAL_CHANGED = """
Your notification interval was changed
"""

INVALID_INTERVAL = """
Invalid interval. Enter interval amount in hours.
"""

USER_DELETED_SUCCESSFULLY = """
Your data and cookies was successfully deleted.
"""