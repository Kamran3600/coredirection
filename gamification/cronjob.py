import logging

from gamification.views import process_and_update_mongo

logger = logging.getLogger(__name__)


def rank_update_job():
    process_and_update_mongo(None)
    logger.info("Cronjob ran successfully")
