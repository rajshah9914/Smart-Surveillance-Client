from firebase import firebase

firebase= firebase.FirebaseApplication("https://sass-cb9b6.firebaseio.com/",None)
# data={
# 'fire':'0',
# 'weapon':'0',
# 'intruder':'0'
# }
# POST
# result= firebase.post('/sass-cb9b6/sass',data)

# GET
result= firebase.get('/sass-cb9b6/sass','')

# UPDATE
# result= firebase.put('/sass-cb9b6/sass/-MENTRivnr1SqB73rmqL','fire','1')
print(result)
print(result['-MENTRivnr1SqB73rmqL']['fire'])
print(result['-MENTRivnr1SqB73rmqL']['intruder'])
print(result['-MENTRivnr1SqB73rmqL']['weapon'])