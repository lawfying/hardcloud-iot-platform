from signals import post_sub
from restapi.models import Datastream
from scheduler.models import Trigger,Action,Parameter

import urllib,urllib2
from rest_framework.authtoken.models import Token

def postdata(token=None,url=None,data=None):
	token = 'Token'+' '+token
	headers = {'Authorization':token}
	#data = {'value':22}
	url = url
	data = urllib.urlencode(data)
	req = urllib2.Request(url,data,headers=headers)
	urllib2.urlopen(req)
	print("post ok")



def callback(sender, **kwargs):
	ds_pk = kwargs['dspk']
	value = float(kwargs['value'])

	try:
		trigger_list = Trigger.objects.filter(datastream_source=ds_pk)
		for trigger in trigger_list:
			token_key = Token.objects.get(user=trigger.owner)
			paras = Parameter.objects.filter(action=trigger.action)
			paras_data = {}
			for paras_tmp in paras:
				paras_data[paras_tmp.key] = paras_tmp.value
			url = trigger.action.action_url
			threshold = float(trigger.threshold_value)
			maximum = float(trigger.maximum)
			minimum = float(trigger.minimum)

			if trigger.compare_choice == 'GREAT_THAN':
				if value > threshold:
					print "gt" + trigger.threshold_value
					postdata(token_key.key,url,paras_data)
			elif  trigger.compare_choice == 'EQUAL':
				if value == threshold:
					postdata(token_key.key,url,paras_data)

			elif  trigger.compare_choice == 'GREAT_EQUAL':
				if value >= threshold:
					postdata(token_key.key,url,paras_data)
			elif  trigger.compare_choice == 'LITTLE_THAN':
				if value < threshold:
					postdata(token_key.key,url,paras_data)
			elif  trigger.compare_choice == 'LITTLE_EQUAL':
				if value <= threshold:
					postdata(token_key.key,url,paras_data)
			elif  trigger.compare_choice == 'BETWEEN_MAX_MIN':
				if value <= maximum and value >= minimum:
					postdata(token_key.key,url,paras_data)
			elif  trigger.compare_choice == 'NOT_BETWEEN_MAX_MIN':
				if value > maximum or value < minimum:
					postdata(token_key.key,url,paras_data)											
			else:
				pass
				
	except Trigger.DoesNotExist:
		pass

post_sub.connect(callback)





