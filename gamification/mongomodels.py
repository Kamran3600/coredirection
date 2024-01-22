from mongoengine import Document, StringField, IntField, connect
import os
from dotenv import load_dotenv
load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/Core_direction')
connect(host=mongodb_uri)


class ChallengeParticipant(Document):
    id = IntField()
    username = StringField()
    firstname = StringField()
    lastname = StringField()
    profile_picture = StringField()
    email = StringField()
    gender = StringField()
    privacy = StringField()
    totalCorePoints = IntField()
    stepCounts = IntField()
    checkins = IntField()
    heart_rate = IntField()
    totalActivityLogToday = IntField()
    rank = IntField()
    numberOfParticipant = IntField()
    challengeID = IntField()
    challengeSlug = StringField()
    totalWatchedVideoToday = IntField()
    meta = {
        'collection': 'challengeparticipantschemas'
    }
