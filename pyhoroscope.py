from lxml import html
import requests
from datetime import datetime, timezone

####################################################################
# API
####################################################################

class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "https://www.horoscop.ro/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date_utc = datetime.now(timezone.utc)
        date_local = str(date_utc.astimezone()).split(' ')[0]
        horoscope = str(tree.xpath("//*[@id=\"postData\"]/div[2]/div[1]/p/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "").replace("[\'", "").replace("\']", "")
        
        dict = {
            'data': date_local,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "https://www.horoscop.ro/horoscop-saptamanal-" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        week = str(tree.xpath("//*[@id=\"postData\"]/h1/text()"))
        week = week.split(sunsign.capitalize())[-1]
        week = week.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath("//*[@id=\"postData\"]/div/div[1]/p/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "").replace("[\'", "").replace("\']", "")
        
        dict = {
            'sapt': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "https://www.horoscop.ro/horoscop-" + sunsign + "-luna"
        response = requests.get(url)
        tree = html.fromstring(response.content)
        month = str(tree.xpath("//*[@id=\"postData\"]/h1/text()"))
        month = month.split('luna')[-1]
        month = month.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath("//*[@id=\"postData\"]/div/div[1]/p/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "").replace("[\'", "").replace("\']", "")
        
        dict = {
            'luna': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        now = datetime.datetime.now()
        year = now.year
        url = "https://www.horoscop.ro/horoscop-" + sunsign + "-" + year
        response = requests.get(url)
        tree = html.fromstring(response.content)
        horoscope = str(tree.xpath("//*[@id=\"postData\"]/div/div[1]/p/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "").replace("[\'", "").replace("\']", "")
        
        dict = {
            'an': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
