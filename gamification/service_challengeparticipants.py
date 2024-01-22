from .mongomodels import ChallengeParticipant
from operator import itemgetter


def update_mongo_participants(users_info, total_participants):
    for index, user_info in enumerate(users_info, start=1):
        ChallengeParticipant.objects(id=user_info['user_id']).update_one(
            upsert=True,
            challengeID=user_info['challengeID'],
            username=user_info['username'],
            firstname=user_info['firstname'],
            lastname=user_info['lastname'],
            email=user_info['email'],
            gender=user_info['gender'],
            privacy=user_info['privacy'],
            stepCounts=user_info['stepCounts'],
            heart_rate=user_info['heart_rate'],
            totalCorePoints=user_info['totalCorePoints'],
            rank=index,
            profile_picture=user_info['profile_picture'],
            challengeSlug=user_info['challengeSlug'],
            totalActivityLogToday=user_info['totalActivityLogToday'],
            totalWatchedVideoToday=user_info['totalWatchedVideoToday'],
            checkins=user_info['checkins'],
            numberOfParticipant=total_participants
        )

        # Optional: Printing for debugging or logging purposes
        print(
            f"Updated user {user_info['user_id']} - "
            f"challengeID: {user_info['challengeID']}, "
            f"username: {user_info['username']}, "
            f"firstname: {user_info['firstname']}, "
            f"lastname: {user_info['lastname']}, "
            f"email: {user_info['email']}, "
            f"gender: {user_info['gender']}, "
            f"privacy: {user_info['privacy']}, "
            f"stepCounts: {user_info['stepCounts']}, "
            f"heart_rate: {user_info['heart_rate']}, "
            f"totalCorePoints: {user_info['totalCorePoints']}, "
            f"rank: {index}, "
            f"profile_picture: {user_info['profile_picture']}, "
            f"challengeSlug: {user_info['challengeSlug']}, "
            f"totalActivityLogToday: {user_info['totalActivityLogToday']}, "
            f"totalWatchedVideoToday: {user_info['totalWatchedVideoToday']}",
            f"checkins: {user_info['checkins']}",
            f"numberOfParticipant: {total_participants}",
        )