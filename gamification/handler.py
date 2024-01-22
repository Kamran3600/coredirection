from .models import GamificationChallenge, GamificationCorePointRecord, UserGamificationChallenge, FosUserUser
from django.db.models import Sum
from django.utils import timezone
from django_rq import job
from .service_challengeparticipants import update_mongo_participants


@job
def process_relevant_challenges(challenge_ids):
    current_time = timezone.now()
    gamif_challenges = GamificationChallenge.objects.filter(
        id__in=challenge_ids, end_date__gt=current_time
    )

    users_info = []

    for challenge in gamif_challenges:
        user_gamification_entries = UserGamificationChallenge.objects.filter(
            gamification_challenge_id=challenge.id,
        )
        for entry in user_gamification_entries:
            user = entry.user

            aggregated_data = GamificationCorePointRecord.objects.filter(
                user=user
            ).aggregate(
                total_points=Sum('day_core_point'),
                total_heart_rate=Sum('heart_rate'),
                total_log_activity=Sum('log_activity'),
                total_on_demand=Sum('ondemand'),
                total_on_booking=Sum('booking'),
                total_steps=Sum('step')
            )

            total_core_points = aggregated_data['total_points'] or 0
            heart_rate = aggregated_data['total_heart_rate'] or 0
            log_activity = aggregated_data['total_log_activity'] or 0
            ondemand = aggregated_data['total_on_demand'] or 0
            booking = aggregated_data['total_on_booking'] or 0
            user_steps = aggregated_data['total_steps'] or 0

            user_info = FosUserUser.objects.values(
                'id', 'username', 'email', 'firstname', 'lastname', 'profile_picture', 'gender', 'privacy'
            ).get(id=user.id)

            users_info.append({
                'user_id': user_info['id'],
                'username': user_info['username'],
                'email': user_info['email'],
                'firstname': user_info['firstname'],
                'lastname': user_info['lastname'],
                'profile_picture': user_info['profile_picture'],
                'gender': user_info['gender'],
                'privacy': user_info['privacy'],
                'challengeID': entry.gamification_challenge_id,
                'rank': entry.rank,
                'totalCorePoints': total_core_points,
                'challengeSlug': challenge.slug_url,
                'stepCounts': user_steps,
                'heart_rate': heart_rate,
                'totalActivityLogToday': log_activity,
                'totalWatchedVideoToday': ondemand,
                'checkins': booking,
            })

    users_info = sorted(users_info, key=lambda x: x['totalCorePoints'], reverse=True)
    total_participants = len(users_info)
    for i, user_info in enumerate(users_info, start=1):
        user_info['rank'] = i

    update_mongo_participants(users_info, total_participants)

    return users_info, total_participants
