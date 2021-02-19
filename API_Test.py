import requests

COOKIE = {'MDD.Web.Prod.Operator.SharedCookie': 'CfDJ8Dn1Vet7b5FBpZowBv1IuXNMlk05EPK09oyQUiJz-Pt2tlVKbU-40B9v7vx8IaVz7aCmqpbs2nFc_AE4kaQT-Jktd0vkwErpqvwnlFNCQOEPg6Vpjz4RAD_0Gmw8tPeCdj6txrfJ-YwofbjzUe00hZX_zzGcMzmfIf1UAcX81lsTq4yo08CSKrLNHgiwk4l0_dp-ajAsofP39WAhwIQVK_OFzXFzD9qIX5s1IibWOuQhBdHkoUBxQZFTKzu7_F4CNPIu9BeGOepB5mNwPQd3bjoipsoDfOkxBIuMp-K1YtoL-DvBjUvlFAws1l59fEPVHb9X4m8s_ShtBL6crQxJU2sAc8XZniGt_0bs-XbQnJmM'}

BASE_URL = '...'

###

root_object_id = requests.get(BASE_URL + 'NdsObjects/GetTreeRootObjectId', verify=False, cookies=COOKIES)
root_object_id = root_object_id.json()['data']
id_tree = root_object_id['rootObjectId']

###

response_tree = requests.get(BASE_URL + 'NdsObjects/GetTree', params={'rootObjectId': id_tree}, verify=False, cookies=COOKIES)

dict_tree = response_tree.json()['data']['root']['children'][0]['children']
list_id_mo = []
for i in dict_tree:
    for c in i['children']:
        for v in c['children']:
            list_id_mo.append(v['data']['ndsObjectId'])

###

r = []
for object_id in list_id_mo:
    print(object_id)
    sleep(1)
    response_owners = requests.get(BASE_URL + 'MddRoads/GetMddRoadOwnerListAsync', params={'ndsObjectId': object_id}, verify=False, cookies=COOKIES)
    assert response_owners.status_code == 200
    assert response_owners.json()['result'] is True
    assert response_owners.json()['data'] is not None
    if response_owners.json()['data'] != []:
        continue
    else:
        print('Нет овнера')
        r.append(object_id)
print(r)
