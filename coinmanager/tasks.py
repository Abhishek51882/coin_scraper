from celery import shared_task
from .models import ScrapingTask
from .scraper import CoinMarketCapScraper

@shared_task
def scrape_coin_data(task_id):
    task = ScrapingTask.objects.get(id=task_id)
    scraper = CoinMarketCapScraper()
    data = scraper.scrape(task.coin)
    task.data = data
    task.status = 'completed'
    task.save()
