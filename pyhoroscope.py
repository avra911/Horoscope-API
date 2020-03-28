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
        
        dict = {
            'date': date_local,
            'horoscope': str(tree.xpath("//*[@id=\"postData\"]/div[2]/div[1]/p/text()")),
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
        horoscope = str(tree.xpath("//*[@id=\"postData\"]/div/div[1]/p/text()"))
        dict = {
            'week': week,
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
        horoscope = str(tree.xpath("//*[@id=\"postData\"]/div/div[1]/p/text()"))
        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        year = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        year = year.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
