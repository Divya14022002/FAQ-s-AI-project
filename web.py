from flask import Flask, render_template, request, jsonify
import re
import long_responses as long

app = Flask("chat")

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty=0
    has_required_words=True
    #counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1
    #Calculates the percent of recognised words in a user message
    percentage=float(message_certainty)/float(len(recognised_words))
    #Checks That the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)
    #Response------------------------------
    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response('I\'m doing fine, and You?',['how','are','you','doing'],required_words=['how'])
    response('Thank You!',['i','love','Industry','academia','community'],required_words=['love','industry','academia','community'])
    response('Go to https://www.industryacademiacommunity.com/courses/Internships',['where','to','apply','for','internship'],required_words=['apply','internship'])
    response('Please join our Telegram Channel https://t.me/+uXmD1vTLpttjN2Vl',['Is','There','any','groups','for','update','or','information'],required_words=['groups','update','any','information'])
    response('There are 16 IT & 7 Management domains for internship: cloud computing,  digital marketing, devOps, human resources, machine learning, data analytics, artificial intelligence, business Research, Web Development, Java, Python,Business Development, React JS, UI/UX, Node.js, Operations Management, Android Development, Quality Assurance, Flutter, Cyber Security, Product Management,  Project Management, Game Development, Blockchain, Full Stack Development, Marketing Management',['What','are','various','the','domain','internship'],required_words=['domain','various','internship'])
    response(long.I_WEEKS,['what','is','the','difference','in','6','8','12', 'weeks','internship'],required_words=['difference','in','6','8','12','weeks'])
    response(long.C_CER,['will','there','be','offer','letters','and','certificates'],required_words=['offer','letters','certificates'])
    response(long.R_EATING,['what','you','eat'],required_words=['you','eat'])
    response(long.H_HELP,['will','participants','get','any','help','during','the','project'],required_words=['participants','help','during','project'])
    response(long.A,['will','participants','get','the','appointment','letter'],required_words=['participants','appointment','letter'])
    response(long.B,['what','is','successful','completion','of','internship'],required_words=['successful','completion','internship'])
    response(long.D,['can','participants','participate','in','more','than','one','domain'],required_words=['participate','more','than','one','domain'])
    response(long.E,['internship','will','be','free','or','paid'],required_words=['free','or','paid'])
    response(long.F,['what','is','the','eligibility','criteria','for','participating','in','this','internship'],required_words=['eligibility','criteria'])
    response(long.G,['can','graduate','and','freshers','apply','for','this','internship'],required_words=['graduate','freshers','apply','internship'])
    response(long.I,['timings','for','internship'],required_words=['timings','internship'])
    response('Yes, Laptop Required.',['do','we','require','laptop','specifically','for','the','projects'],required_words=['require','laptop','specifically','projects'])
    response(long.J,['how','to','choose','the','domain'],required_words=['choose','domain','how'])
    response('Yes, the data will be provided for data analytics.',['will','data','be','provided','for','data','analytics','internship'],required_words=['data','provided','data','analytics','internship'])
    response(long.K,['what','is','industry','academia','community','IAC'],required_words=['what','industry','academia','community','IAC'])
    response(long.L,['what','are','the','benefits','of','being','part','of','IAC'],required_words=['benefits','being','part','of','IAC'])
    response(long.M,['how','will','the','internship','be','conducted'],required_words=['how','will','internship','conducted'])
    response(long.N,['has','this','program','helped','students','earlier'],required_words=['program','helped','students','earlier'])
    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)
    

    return long.unknown() if highest_prob_list[best_match]<1 else best_match



def get_response(user_input):
   split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
   response=check_all_messages(split_message)
   return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    bot_response = get_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
