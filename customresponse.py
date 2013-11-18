# -*- coding: utf-8 -*-
##hexmessages are obtained at http://api.mvaayoo.com/unicodeutil/unicode.jsp
from urllib import urlencode, urlopen
import binascii
from myconfig import mvayooUsername, mvayoopassword

def sendSMS(number, inputMessage):
    strUrl =  "http://api.mVaayoo.com/mvaayooapi/MessageCompose?"
    param = {}
    param['user'] = mvayooUsername+":"+mvayoopassword ## account:pass
    param['senderID'] = "TEST SMS" ## Because nothing else works
    param['receipientno'] = number[-10:] ## Last 10 digits of the number
    param['msgtype'] = "4" ## For Unicode messages
    param['dcs'] = "8" ## For UTF-8
    param['ishex'] = "1" ## If message in hexadecimal
    param['msgtxt'] = inputMessage
    param['state'] = "4"
    url = strUrl + (urlencode(param))
    print url
    imiResponse = urlopen(url).read ()
    return imiResponse


def sendSMSGujarati(number, inputStatus, inputMessage):
    if (inputStatus == "SMS_SUBMISSION_ACCEPTED"):
        #message = "તમારી માહિતી સ્વીકાર્ય છે। આભાર।"
        hexmessage = "0aa40aae0abe0ab00ac000200aae0abe0ab90abf0aa40ac000200ab80acd0ab50ac00a950abe0ab00acd0aaf00200a9b0ac7096400200a860aad0abe0ab00964"
        return sendSMS(number, hexmessage)
    elif(inputStatus == "SMS_PARSING_ERROR"):
        #message = "તમે આપેલ માહિતી મા ભૂલ છે। માહિટિ સુધારી ફરી મોક્લો  અથવા દર્શાવેલ નંબર 9537675599 પર સંપર્ક કરો। આભાર।"
        hexmessage = "0aa40aae0ac700200a860aaa0ac70ab200200aae0abe0ab90abf0aa40ac000200aae0abe00200aad0ac20ab200200a9b0ac7096400200aae0abe0ab90abf0a9f0abf00200ab80ac10aa70abe0ab00ac000200aab0ab00ac000200aae0acb0a950acd0ab20acb002000200a850aa50ab50abe00200aa60ab00acd0ab60abe0ab50ac70ab200200aa80a820aac0ab00020003900350033003700360037003500350039003900200aaa0ab000200ab80a820aaa0ab00acd0a9500200a950ab00acb096400200a860aad0abe0ab00964"
        return sendSMS(number, hexmessage)
    else:
        #message = "હમણા તમારી માહિતી સ્વીકાર્ય નથી। થોડા સમય પછી પ્રયત્ન કરવા નમ્ર વિનતી। આભાર।"
        hexmessage = "0ab90aae0aa30abe00200aa40aae0abe0ab00ac000200aae0abe0ab90abf0aa40ac000200ab80acd0ab50ac00a950abe0ab00acd0aaf00200aa80aa50ac0096400200aa50acb0aa10abe00200ab80aae0aaf00200aaa0a9b0ac000200aaa0acd0ab00aaf0aa40acd0aa800200a950ab00ab50abe00200aa80aae0acd0ab000200ab50abf0aa80aa40ac0096400200a860aad0abe0ab00964"
        return sendSMS(number, hexmessage)
