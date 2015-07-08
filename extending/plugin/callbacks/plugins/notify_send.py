from subprocess import call

def notify_send(title, message, icon):
    call(["notify-send", title, message,"-i", icon])

class CallbackModule(object):

    def runner_on_failed(self, host, res, ignore_errors=False):
        notify_send(
                    "ANSIBLE FAILURE",
                    "Host: %s\nModule: %s\nMessage: %s" % (
                                                           host,
                                                           res.get('invocation').get('module_name'),
                                                           res.get('msg')
                                                          ),
                    "dialog-warning"
                   )
