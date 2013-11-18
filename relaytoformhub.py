from webapp2 import WSGIApplication,RequestHandler
from urllib import urlencode, urlopen
from ast import literal_eval
from customresponse import sendSMSGujarati


def postToFormhub(number, message):
    formurl = "https://formhub.org/cipt/sms_submission?"
    param = {}
    param['identity'] = number
    param['text'] = message
    url = formurl + (urlencode(param))
    data = urlopen(url).read()
    data = literal_eval(data)
    return data

        
class MyRequestHandler(RequestHandler):
    
    def get(self):
        number = self.request.get('msisdn')
        message = self.request.get('sms')
        circle = self.request.get('circle')
        opnm = self.request.get('opnm')
        datetime = self.request.get('datetime')

        if (number == '') and (message == '') and (circle == '') and (opnm == '') and (datetime == ''):
            self.response.write("Hi there! Looks like you are lost.")
            
        elif (number == '') or (message == ''):
            self.response.out.write("Error")
            
        else:
            message = str(message).split('CIPT ')[1]
            FormhubResponse = postToFormhub(number, message)
            FormhubResponseStatus = FormhubResponse['status']
            FormhubResponseMessage = FormhubResponse['message']
            #self.response.out.writeFormhubResponse)
            self.response.out.write(FormhubResponseStatus)
            sendSMSGujarati(number,FormhubResponseStatus, FormhubResponseMessage)
            
            if (FormhubResponseStatus != "SMS_SUBMISSION_ACCEPTED"):
                wasteMessagePrefix = "waste *4 " +number+" *5 "
                wasteMessageSuffix = " *6 " + FormhubResponseMessage
                FormhubResponse = postToFormhub(number, wasteMessagePrefix +message +wasteMessageSuffix)
                            
    def post(self):
        self.response.write("Use GET request.")
            
class MainPage(RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('')
        
application = WSGIApplication([('/', MyRequestHandler),], debug=True)
