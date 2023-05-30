import pysnow
# from jenkins import Jenkins
from time import sleep

host = "na-access-control.dc04.hosted.exlibrisgroup.com"
username = "24x7hub@root@infra01.dc04.hosted.exlibrisgroup.com"
password = "Cloudseyes123!"

# server = Jenkins('http://jenkins-na.int.hosted.exlibrisgroup.com:8080', username='fgl_jenk_update', password='6R*d12@SRd!8F8#uS&YXpYn!')
# server = Jenkins('http://jenkins-na.int.hosted.exlibrisgroup.com:8080', username='24x7hub', password='Cloudseyes123!')
c = pysnow.Client(instance='exlprod', user='api.user@exlibrisgroup.com', password='MisIntegrationUser!')
incident = c.resource(api_path='/table/incident')
incidents = incident.get(query='assignment_group=cd463a84db9f7240ac07f9851d9619f4^stateNOT IN2,6,7,8^short_descriptionNOT LIKEcancellation^short_description=Ansible-Last-Run-Check').all()

result = incident.delete(query={'number': 'INC0612530'})
