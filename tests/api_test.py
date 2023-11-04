import logging
import requests
from yaml_reader import data


class TestApi:
    def test_post_create(self, user_login):
        res = requests.Session().post(url=data['address_post'], headers={'X-Auth-Token': user_login},
                                      data={'title': data['title'], 'description': data['description'],
                                            'content': data['content']})
        logging.debug(f"Response is {str(res)}")
        assert str(res) == '<Response [200]>', 'post_create FAIL'

    def test_check_post_create(self, user_login):
        result = requests.Session().get(url=data['api_address'], headers={'X-Auth-Token': user_login}).json()['data']
        logging.debug(f"get request return: {result}")
        list_description = [i['description'] for i in result]
        assert data['description'] in list_description, 'check_post_create FAIL'

    def test_check_notme_post(self, user_login):
        result = requests.Session().get(url=data['api_address'], headers={'X-Auth-Token': user_login},
                                        params={'owner': 'notMe'}).json()['data']
        logging.debug(f"get request return: {result}")
        result_title = [i['title'] for i in result]
        assert data['not_me_title'] in result_title, 'check not me post FAIL'
